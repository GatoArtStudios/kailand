import Flecha from "../../assets/img/flecha.svg";

export default function ButtonScrollDownloads() {
    return (
        <div className="w-16">
            <a href="/downloads/#smartscreen" className="no-decorect cursor-crosshair group">
                <div className="group-hover:animate-bounce animate-pulse group-hover:bg-black/30 rounded-full p-2">
                    <img src={Flecha.src} alt="Boton para ver sobre SmartScreen" className="h-12 w-12"/>
                </div>
            </a>
        </div>
    )
}