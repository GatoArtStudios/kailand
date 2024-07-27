import React, { useState, useEffect } from "react";
import Inicio from "./Inicio.jsx";
import ButtomWiki from "./react/ButtomWiki.jsx";
import Guia from "./Guia.jsx";
import Mods from "./Mods.jsx";
import Launcher from "./Launcher.jsx";
import Bugs from "./Bugs.jsx";
import Juego from "./Juego.jsx";
import Comunicados from "./Comunicados.jsx";
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
            case 'guia':
                return <Guia />;
            case 'mods':
                return <Mods />;
            case 'launcher':
                return <Launcher />;
            case 'bugs':
                return <Bugs />;
            case 'juego':
                return <Juego />;
            case 'comunicados':
                return <Comunicados />;
            default:
                return <Inicio />;
        }
    };

    return (
        <div className="flex lg:flex-row text-white lg:p-10 min-[200px]:p-3 h-screen min-[200px]:flex-col min-[200px]:items-center lg:items-start">
            <div className="px-5 lg:w-1/5 min-[200px]:w-full flex flex-col lg:items-start min-[200px]:items-center">
                <ButtomWiki text='Inicio' onClick={() => setPage('inicio')} />
                <ButtomWiki text='Guía' onClick={() => setPage('guia')} />
                <ButtomWiki text='Mods' onClick={() => setPage('mods')} />
                <ButtomWiki text='Launcher' onClick={() => setPage('launcher')} />
                <ButtomWiki text='Bugs' onClick={() => setPage('bugs')} />
                <ButtomWiki text='Juego' onClick={() => setPage('juego')} />
                <ButtomWiki text='Comunicados' onClick={() => setPage('comunicados')} />
            </div>
            <div className="lg:w-4/5 min-[200px]:w-11/12 py-9 lg:px-14 min-[200px]:px-5 backdrop-blur-md bg-black/30 rounded-xl overflow-auto hide-scrollbar h-screen">{renderPage()}</div>
        </div>
    );
}

export default App;