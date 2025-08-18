import os, subprocess, tempfile, shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pylatexenc.latexencode import unicode_to_latex
from ..config import settings

def sanitize(value: str) -> str:
    # minimal LaTeX escaping
    return unicode_to_latex(value or "")

def render_tex(template_dir: str, template_name: str, context: dict) -> str:
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(enabled_extensions=("tex",), default_for_string=False)
    )
    env.filters["latex"] = sanitize
    tpl = env.get_template(template_name)
    return tpl.render(**context)

def compile_pdf(latex_source: str, jobname: str) -> str:
    build_dir = settings.BUILD_DIR
    os.makedirs(build_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        texfile = os.path.join(tmp, f"{jobname}.tex")
        with open(texfile, "w", encoding="utf-8") as f:
            f.write(latex_source)
        subprocess.run(["latexmk", "-pdf", "-xelatex", "-interaction=nonstopmode", texfile],
                       cwd=tmp, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pdf_src = os.path.join(tmp, f"{jobname}.pdf")
        pdf_dst = os.path.join(build_dir, f"{jobname}.pdf")
        shutil.copyfile(pdf_src, pdf_dst)
        return pdf_dst

def render_resume(data, template_path):
    # TODO: Implement real LaTeX rendering
    return "/static/sample.pdf"