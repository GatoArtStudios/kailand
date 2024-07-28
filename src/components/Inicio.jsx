import TitleWiki from "./react/TitleWiki";
import SubTitleWiki from "./react/SubTitleWiki";
import Nota from "./react/Nota";
import ParLeft from "./react/ParLeft";
import Link from "./react/Link";

export default function Inicio() {
    return (
        <div className="flex flex-col justify-center items-center">
            <TitleWiki text="Bienvenido sobreviviente" />
            <ParLeft>
            ¡Espero que esta Wiki de KAILAND V pueda resolver todas tus dudas y otorgarte la información que necesites!
            </ParLeft>
            <SubTitleWiki text="¿Qué es Kailand V? 🤔" />
            <ParLeft>
                KAILAND es un servidor/serie de Minecraft. Esta temporada semi-anárquica es apocalíptica, por lo que deberás sobrevivir en un mundo peligroso y destructivo, protegiendo a los tuyos con todo el contenido que ofrecemos para ti.
            </ParLeft>
            <ParLeft>
            De cualquier manera, puedes abrir un ticket o escribir por el canal de general en nuestro servidor de <Link text="Discord" href="https://kailand.es/discord" /> cualquier duda que tengas. Intenta leerte toda la wiki o solo los apartados donde tu creas que puede estar la información que estés buscando. 
            </ParLeft>
            <Nota>
            ¡Únete a nuestro <Link href="https://kailand.es/discord" text="Discord" /> para que te enteres de todo lo nuevo de Kailand!.
            te recomendamos leer las reglas del servidor en discord y en el launcher, ten muy en cuenta el apartado de Guía, Launcher y Comunicados, serán muy importantes para solucionar dudas y posibles bugs.
            </Nota>
        </div>
    );
}