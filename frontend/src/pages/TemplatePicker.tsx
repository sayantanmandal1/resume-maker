import { useEffect, useState } from "react";
import api from "../api/client";
import { useNavigate } from "react-router-dom";

export default function TemplatePicker(){
  const [templates, setTemplates] = useState<any[]>([]);
  const [selected, setSelected] = useState<string>("");
  const [title, setTitle] = useState("My Resume");
  const navigate = useNavigate();

  useEffect(()=>{ (async()=>{
    const {data} = await api.get("/templates"); setTemplates(data);
  })(); },[]);

  const create = async ()=>{
    if(!selected) return;
    const {data} = await api.post("/resumes", { user_id:1, template_slug:selected, title });
    localStorage.setItem("resume_id", data.resume_id);
    navigate("/editor");
  };

  return (
    <div className="grid">
      <div className="card">
        <h3>Select a template</h3>
        <div className="grid" style={{gridTemplateColumns:"repeat(4, 1fr)"}}>
          {templates.map(t=>(
            <label key={t.slug} className="card" style={{cursor:"pointer"}}>
              <input type="radio" name="tpl" onChange={()=>setSelected(t.slug)}/>
              <div><img src={t.thumbnail_url} alt={t.name} style={{width:"100%", borderRadius:8}}/></div>
              <div className="section-title">{t.name}</div>
            </label>
          ))}
        </div>
      </div>
      <div className="card">
        <label>Resume Title</label>
        <input value={title} onChange={e=>setTitle(e.target.value)} />
        <br/><button className="button" onClick={create}>Start Editing</button>
      </div>
    </div>
  );
}
