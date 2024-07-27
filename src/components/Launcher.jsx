import TitleWiki from "./react/TitleWiki";
import ParLeft from "./react/ParLeft";

export default function Launcher() {
    return (
        <div className="flex flex-col justify-center items-center">
            <TitleWiki text="Sobre el Launcher" />
            <ParLeft>
                <li className="my-5">
                El launcher de Kailand tiene un Anticheat, por lo que, en la carpeta de “mods” (dentro de la carpeta de “.kailand”) no podrán modificar, ni cambiar nada con relación al paquete de mods original de Kailand. Lo mismo pasa con la carpeta “resourcepacks”, pero de una manera menos estricta, para permitir que los usuarios usen sus Packs de Texturas preferidos.
                </li>
                <li className="my-5">
                Los jugadores que tengan el mínimo de RAM (8 GB DRR3) se les recomienda usar todos los mods de rendimiento del Launcher en la sección de “Predeterminados”: Rubidium, FPS Reducer, Better FPS y el Rubidium Extras que se encuentra “Recomendados”.
                </li>
                <li className="my-5">
                NO cambiar la versión de Java que viene configurada, ya que es la versión específica recomendada que te instala Mojang por defecto. Por lo que NO se necesita instalar ninguna otra versión de java.
                </li>
                <li className="my-5">
                En el apartado “Consola” podrás ver y monitorear el Debug del Launcher, eso quiere decir que, todos los procesos que haga el Launcher y todas las opciones que clickees estarán a la vista.
                </li>
                <li className="my-5">
                En el apartado de “Perfil” y en la opción “Tipo de cuenta” NO está disponible la alternativa “(Online) Microsoft”. Debido a que, hasta el momento no ha habido integración con la API de Mojang, por el momento…
                </li>
            </ParLeft>
        </div>
    );
}