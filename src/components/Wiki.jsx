import React, { useState, useEffect } from "react";
import Inicio from "./Inicio.jsx";
import ButtomWiki from "./ButtomWiki.jsx";
import Ingreso from "./Ingreso.jsx";
import Mods from "./Mods.jsx";
import Launcher from "./Launcher.jsx";
import Crafteos from "./Crafteos.jsx";
import Bugs from "./Bugs.jsx";
import Juego from "./Juego.jsx";
import "../styles/hidden_scroll.css";

const App = ({ slug }) => {
    const [page, setPage] = useState( slug || 'inicio');

    useEffect(() => {
        if (slug && slug !== page) {
            setPage(slug);
        }
    }, [slug]);

    const renderPage = () => {
        switch (page) {
            case 'inicio':
                return <Inicio />;
            case 'ingreso':
                return <Ingreso />;
            case 'mods':
                return <Mods />;
            case 'launcher':
                return <Launcher />;
            case 'crafteos':
                return <Crafteos />;
            case 'bugs':
                return <Bugs />;
            case 'juego':
                return <Juego />;
            default:
                return <Inicio />;
        }
    };

    return (
        <div className="flex flex-row text-white p-10 h-screen">
            <div className="px-5 w-1/5 flex flex-col">
                <ButtomWiki text='Inicio' onClick={() => setPage('inicio')} />
                <ButtomWiki text='Ingreso' onClick={() => setPage('ingreso')} />
                <ButtomWiki text='Mods' onClick={() => setPage('mods')} />
                <ButtomWiki text='Launcher' onClick={() => setPage('launcher')} />
                <ButtomWiki text='Crafteos' onClick={() => setPage('crafteos')} />
                <ButtomWiki text='Bugs' onClick={() => setPage('bugs')} />
                <ButtomWiki text='Juego' onClick={() => setPage('juego')} />
            </div>
            <div className="w-4/5 p-9 bg-black rounded-xl overflow-auto hide-scrollbar">{renderPage()}</div>
        </div>
    );
}

export default App;