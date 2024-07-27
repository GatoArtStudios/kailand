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
            <SubTitleWiki text="¿Qué es KAILAND V?" />
            <ParLeft>
                KAILAND es un servidor/serie de Minecraft. Esta temporada semi-anárquica es apocalíptica, por lo que deberás sobrevivir en un mundo peligroso y destructivo, protegiendo a los tuyos con todo el contenido que ofrecemos para ti.
            </ParLeft>
            <Nota>
            ¡Únete a nuestro <Link href="https://kailand.es/discord" text="Discord" /> para que te enteres de todo lo nuevo de Kailand!
            </Nota>
        </div>
    );
}