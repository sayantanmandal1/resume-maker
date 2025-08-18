import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import TemplatePicker from "./pages/TemplatePicker";
import ResumeEditor from "./pages/ResumeEditor";
import "./styles/globals.css";

export default function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <header className="grid" style={{gridTemplateColumns:"auto 1fr auto", alignItems:"center"}}>
          <h2>AI Resume Lab</h2>
          <nav><Link to="/">Templates</Link> &nbsp; | &nbsp; <Link to="/editor">Editor</Link></nav>
          <div className="badge">Postgres • FastAPI • CRA</div>
        </header>
        <Routes>
          <Route path="/" element={<TemplatePicker/>}/>
          <Route path="/editor" element={<ResumeEditor/>}/>
        </Routes>
      </div>
    </BrowserRouter>
  );
}
