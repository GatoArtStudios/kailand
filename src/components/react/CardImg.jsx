import React, { useState } from 'react';

export default function CardImg({ ImgSrc, heightImg }) {
    const [isZoomed, setIsZoomed] = useState(false);

    const toggleZoom = () => {
        setIsZoomed(!isZoomed);
    };

    return (
            <div className={`relative block p-3 w-full cursor-pointer ${isZoomed ? 'scale-125 transition duration-300 ease-in-out z-10' : 'scale-100 transition duration-300 ease-in-out z-0'}`} onClick={toggleZoom}>
                <img src={ImgSrc} className={`w-full ${heightImg} rounded-lg ${isZoomed ? 'rounded-md border-green-500/30 border-[1px]' : 'rounded-2xl border-green-500/0'}`} />
            </div>
    )
}