import { useEffect, useMemo, useState } from "react";
import api from "../api/client";

const emptyData = { personal:{}, education:[], experience:[], projects:[], skills:[], awards:[] };

export default function ResumeEditor(){
  const id = localStorage.getItem("resume_id");
  const [data, setData] = useState<any>(emptyData);
  const [pdfUrl, setPdfUrl] = useState<string>("");

  const debounced = useMemo(()=>{
    let t:any; return (fn:Function)=>{ clearTimeout(t); t = setTimeout(()=>fn(), 600); };
  },[]);

  const save = async ()=>{
    await api.post(`/resumes/${id}/versions`, data);
    const {data:rend} = await api.post(`/resumes/${id}/render`);
    setPdfUrl(`http://localhost:8000/static?f=${encodeURIComponent(rend.pdf_path)}#${Date.now()}`);
  };

  useEffect(()=>{ debounced(save); }, [data, debounced]);

  return (
    <div className="grid two">
      <div className="card">
        <h3>Editor</h3>
        <label>Name</label>
        <input value={data.personal.name||""} onChange={e=>setData({...data, personal:{...data.personal, name:e.target.value}})}/>
        <label>Summary</label>
        <textarea value={data.personal.summary||""} onChange={e=>setData({...data, personal:{...data.personal, summary:e.target.value}})} />
        {/* TODO: add sections for education/experience/projects with add/remove/reorder */}
        <button className="button" onClick={save}>Save & Render</button>
      </div>
      <div className="card">
        <h3>Live Preview</h3>
        {pdfUrl ? <iframe title="preview" src={pdfUrl} style={{width:"100%", height:"80vh", border:"none"}}/> : <div className="badge">Type to generate preview...</div>}
      </div>
    </div>
  );
}
