import TitleWiki from "./react/TitleWiki";
import SubTitleWiki from "./react/SubTitleWiki";
import ParLeft from "./react/ParLeft";
import Link from "./react/Link";
import Spam from "./react/Spam";

export default function Launcher() {
    return (
        <div className="flex flex-col justify-center items-center">
            <TitleWiki text="Sobre el Launcher 🚀" />
            <ParLeft>
            Este es el instalador oficial del <Link href="https://kailand.es/downloads" text="Launcher" />. El Launcher de Kailand V, en esta versión se a modificado completamente el código para agregarle encriptado al 
            Launcher y así proteger los archivos de configuración y evitar bypass en el <Spam text="AntiCheat" />, 
            ya que el launcher tiene mucha automatización, hace que dure mas tiempo de carga al abrir el Launcher, si presenta un error al abrir el launcher, solo tienes 
            que eliminar la carpeta <Spam text="versions" /> en el directorio de <Spam text="%appdata%/Roaming/.kailand"/>, en esta versión del Launcher, tenemos versión del launcher tanto 
            como para windows como para linux, el archivo de windows es un instalador, y el de linux es un ejecutable comprimidor en <Spam text="tar" />, es solo descargar, descomprimir y 
            ejecutar <Spam text="./kailand" /> y listo a disfrutar del juego, muchas gracias por ser parte de este proyecto.
            </ParLeft>
            <SubTitleWiki text="Uso en Windows 🖥️" />
            <ParLeft>
            La instalación en Windows, es muy sencillo. Descargar el instalador y ejecutar el archivo descargado (encontraras mas información en la 
            parte inferior del apartado de <Link text="Downloads" href="https://kailand.es/downloads/#smartscreen" /> sobre SmartScreen), y sobre los requisitos de hardware para poder jugara a Kailand V, lo encontraras en la misma sección de downloads en <Link text="Requisitos del sistema" href="https://kailand.es/downloads/#requisitos" />. 
            Si tienes una versión anterior del Launcher, 
            cuando descargues la última, automáticamente se actualiza, por lo que no tienes que eliminar nada (solamente el instalador si deseas). 
            Si presentas algún bug, puedes reportarlo a los Staff del servidor de <Link text="Discord." href="https://kailand.es/discord" />
            </ParLeft>
            <SubTitleWiki text="Uso en Linux 👨‍💻" />
            <ParLeft>
            Por el lado de Linux tenemos un archivo comprimido, aclaro que la versión fue compilada para 64 bits (por el momento no contamos con una versión 
            compilada para 32 bits). Requieres tener la herramienta de tar para extraer el contenido del comprimido, si no lo tiene instalado es solo usar el 
            comando <Spam text="sudo apt install tar" /> para distribuciones <Spam text="Debian/Ubuntu/Otros" />, puede usar <Spam text="sudo pacman -S tar" />, para descomprimir el archivo 
            comprimido, usa el comando <Spam text="tar -xvf kailand-linux-2-0-1-1.tar.gz" /> y te dejara una carpeta llamada linux ingresas a ella con cd linux y debes darle 
            permisos de ejecucion con <Spam text="chmod +x Kailand" /> y luego ejecutarlo con <Spam text="./Kailand" /> y listo, a disfrutar del servidor de Kailand.
            </ParLeft>
            <SubTitleWiki text="Solución a bugs 🐞" />
            <ParLeft>
                <ul className="list-disc list-outside">
                    <li className="my-5">
                    El launcher de Kailand tiene un Anticheat, por lo que, en la carpeta de <Spam text="'mods'" /> (dentro de la carpeta de <Spam text="'.kailand'" /> ) no podrán modificar, 
                    ni cambiar nada con relación al paquete de mods original de Kailand. Lo mismo pasa con la carpeta <Spam text="'resourcepacks'" />, pero de una manera 
                    menos estricta, para permitir que los usuarios usen sus Packs de Texturas preferidos.Si presenta problemas al abrir el Launcher, ya sea 
                    en Linux o Windows, la solución es eliminar la carpeta <Spam text="'versions'" /> , en Windows se encuentra en la ruta <Spam text="%APPDATA%/Roaming/.kailand/versions" />. Por el 
                    lado de Linux se encuentra en <Spam text="$HOME/.kailand/versions" />, si presentas problemas, solo debes eliminar esa carpeta, luego debe cerrar el Launcher 
                    y abrirlo nuevamente, aceptar la notificación para instalar y reparar los recursos del Launcher y del juego. Por favor, NO eliminar 
                    ningún otro archivo, lo cual puede generar inestabilidades o futuros bugs en el juego, si no logra solucionar el problema con el Launcher o 
                    el juego, recuerda comunicarte con un miembro nuestro Staff del servidor de <Link text="Discord." href="https://kailand.es/discord" />
                    </li>
                    <li className="my-5">
                    El mod de <Spam text="'Rubidium'" /> y sus dos dependientes, no son compatibles con todos los equipos que usan Windows, es poco probable pero, en algunos 
                    equipos donde se hacen los testeos correspondientes, ese mod no es compatible en 1/50 equipos. La solución, si un usuario presenta el 
                    problema es, ir al apartado de mods <Spam text="'Predeterminados'" /> y desactivarlo. Una forma rápida de identificar el problema de <Spam text="'Rubidium'" />, se ve 
                    reflejado cuando el juego solo carga un 10% y se queda colgado o no responde. Por otro lado, en equipos con Linux no presentan 
                    ningún problema de los 50 equipos probados, esto quiere decir que, tiene 100% de compatibilidad con Linux en cuanto a ese mod.
                    </li>
                    <li className="my-5">
                    En cuanto al mod <Spam text="'Fancymenu'" /> y sus dependientes, en sistemas operativos con Windows Managers Customs personalizados, el mod bloqueara la carga del juego cuando va a un 70% (los Windows Managers Customs se encuentran presentes en derivados de Windows, es decir, versiones de Windows personalizadas o distribuciones Linux). La forma de detectar este problema es que, la pantalla de carga del juego se queda al 70% de la carga, y la única solución en este caso es ir al apartado de "Mods" y en la opción de "Predeterminados" desactivar el FancyMenu.
                    </li>
                </ul>
            </ParLeft>
            <SubTitleWiki text="Notas📔" />
            <ParLeft>
            <ul className="list-disc list-outside">
                <li className="my-5">
                El launcher de Kailand tiene un Anticheat, por lo que, en la carpeta de <Spam text="'mods'" /> (dentro de la carpeta de <Spam text="%APPDATA%/Roaming/.kailand" />) no podrán modificar, ni cambiar nada con relación al paquete de mods original de Kailand. Lo mismo pasa con la carpeta <Spam text="'resourcepacks'" />, pero de una manera menos estricta, para permitir que los usuarios usen sus Packs de Texturas preferidos.
                </li>
                <li className="my-5">
                <Spam text="NO cambiar la versión de Java que viene configurada" />, ya que es la versión específica recomendada que te instala Mojang por defecto. Por lo que NO se necesita instalar ninguna otra versión de java.
                </li>
                <li className="my-5">
                En el apartado de <Spam text="Consola" /> podrás ver y monitorear el Debug del Launcher, eso quiere decir que, todos los procesos que haga el Launcher y todas las opciones que clickees estarán a la vista.
                </li>
                <li className="my-5">
                En el apartado de <Spam text="Perfil" /> y en la opción <Spam text="Tipo de cuenta" /> NO está disponible la alternativa <Spam text="(Online) Microsoft" />. Debido a que, hasta el momento no ha habido integración con la <Spam text="API de Mojang" />, por el momento…
                </li>
            </ul>
            </ParLeft>
        </div>
    );
}