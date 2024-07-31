import { useState } from "react";
import Link from "./Link";
import Spam from "./Spam";
import AdvertNota from "./AdvertNota"
import Nota from "./Nota"

export default function HoverModWiki({ name, href, description, disponible, file }) {
    const [showTooltip, setShowTooltip] = useState(false);

    const handleMouseOver = () => {
        setShowTooltip(true);
    };

    const handleMouseOut = () => {
        setShowTooltip(false);
    };

    return (
        <div className="relative inline-block">
            <span onMouseOver={handleMouseOver} onMouseOut={handleMouseOut}>
                <Link href={href == 'None' ? '' : href} text={name} />
                <div className={`absolute ${showTooltip ? 'inline-block' : 'hidden'} border-[1px] border-white border-opacity-10 bg-gradient-to-tr from-gray-900 to-transparent text-white rounded-lg p-2 mt-2 translate-x-20 -translate-y-4 w-96 w-max-96 z-30 whitespace-normal`}>
                    {description}
                    <br/>
                    <Spam text={`File: ${file}`} />
                    <br/>
                    {href == 'None' && (
                        <AdvertNota>
                            Documentacion no Disponible
                        </AdvertNota>
                    )}
                </div>
            </span>
        </div>
    )

}