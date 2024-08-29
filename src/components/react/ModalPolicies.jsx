import React, { useState, useEffect } from "react";

export default function ModalPolicies({ href }) {
    const [isAccepted, setIsAccepted] = useState(false);

    const handleAcceptChange = () => {
        setIsAccepted(!isAccepted);
    };
    return (
        <div 
            className="
                border-[1px] 
                border-white 
                border-opacity-10 
                bg-gradient-to-tr 
                from-gray-900 
                to-black/70 
                z-50 
                h-fit 
                w-96 
                rounded-xl 
                p-5
                hidden
            "
            id="modal_policies"
            >
            <h2 className="text-xl font-bold mb-4">Políticas de Privacidad</h2>
            <p className="mb-4 text-lg">
                Kailand utiliza la información proporcionada por los usuarios para
                asegurar una experiencia de juego segura. No vendemos ni compartimos
                su información personal sin su consentimiento, excepto en caso de orden
                judicial. Para más detalles, revise nuestras <a href={href} className="text-blue-500 underline" target="_blank" rel="noopener noreferrer">
                políticas de privacidad completas
                </a>.
            </p>
            <div className="flex items-center mb-4">
                <input 
                type="checkbox" 
                id="accept_policies" 
                className="mr-2" 
                checked={isAccepted} 
                onChange={handleAcceptChange} 
                />
                <label htmlFor="accept_policies" className="text-sm">
                Acepto las políticas de privacidad
                </label>
            </div>
            <div className="hidden" id="link_descargar"></div>
            <p 
                id="link_avaliable" 
                className={`px-4 py-2 rounded cursor-pointer text-center ${isAccepted ? `bg-green-600 text-white avaliable` : 'bg-gray-400 text-gray-700 cursor-not-allowed'}`} 
            >
                Descargar
            </p>
        </div>
    );
}