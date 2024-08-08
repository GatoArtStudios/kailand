import TitleWiki from "./react/TitleWiki";
import ParLeft from "./react/ParLeft";
import Spam from "./react/Spam";
import Link from "./react/Link";
import Nota from "./react/Nota";
import AlertNota from "./react/AlertNota";

export default function Ingreso() {
    return (
        <div className="flex flex-col justify-center items-center">
            <TitleWiki text="Guía de Ingreso 📝" />
            <ParLeft>
            ¡Si tienes pensado ingresar al server, por favor, lea todas las Reglas del Servidor para evitar futuras sanciones y malentendidos!
            </ParLeft>
            <ParLeft>
                <b>Paso 1:</b> Entra a nuestro servidor de <Link href="https://kailand.es/discord" text="Discord" /> o ingresa a nuestra <Link href="https://kailand.es" text="página web." />
            </ParLeft>
            <ParLeft>
                <b>Paso 2:</b> Descarga el <Link href="https://kailand.es/downloads" text="Launcher" /> que se encuentra en la parte superior de de la página de KAILAND V. OJO, no requiere ninguna instalación de Java, ni de ninguna versión de Forge.
            </ParLeft>
            <ParLeft>
                <b>Paso 3:</b> Escoge la versión de tu sistema operativo. Para Windows es recomendado el <Spam text="Instalador" />.
            </ParLeft>
            <Nota>
            Si descargaste el archivo “zip” solo tienes que seleccionar la opción que dice “Extraer aquí” y ya tendrás el ejecutable para abrir el Launcher :D.
            </Nota>
            <ParLeft>
                <b>Paso 4:</b> Abre o <Spam text="ejecuta el Launcher" /> e instala los recursos necesarios que te pide (Estos recursos son: Mods, Java, configuraciones, Forge, entre otros).
            </ParLeft>
            <ParLeft>
                <b>Paso 5:</b> Seleccionas el apartado de <Spam text="Perfil" />. Después, escribes tu nombre de usuario (También puedes colocar el nombre de tu cuenta Premiun si deseas). Posteriormente, le das ak botón <Spam text="Guardar." />
            </ParLeft>
            <ParLeft>
                <b>Paso 6:</b> Seleccionas el apartado de <Spam text="Mods" /> y podrás escoger los mods de tu preferencia. Te recomendamos dejar activado y activar 
                los de rendimiento (No importa si tienes una PC con buenos componentes), en la sección de <Spam text="Predeterminados" />: Rubidium, FPS Reducer, 
                Better FPS, y en la sección de <Spam text="Recomendados" />: Rubidium Extras. Cabe recalcar que, cuando desactivas cualquier opción, automáticamente 
                se elimina el archivo, y si lo vuelves a activar se descargar nuevamente.
            </ParLeft>
            <AlertNota>
                No se recomienda jugar Kailand sin estos mods de rendimiento.
            </AlertNota>
            <ParLeft>
                <b>Paso 7:</b> Dirígete al apartado de <Spam text="Ajustes" /> y selecciona la mitad de la memoria <Spam text="RAM" /> de la cantidad total que te muestra el Launcher, ya que él mismo se encarga de detectar cuánta memoria RAM tienes disponible en tu computador. Cabe aclarar que, no es necesario poner más de <Spam text="10Gb de memoria RAM" /> con configuraciones medias en el juego. 
            </ParLeft>
            <ParLeft>
                <b>Paso 8:</b> Clickea el botón de <Spam text="Jugar" /> del Launcher y dentro del Juego. Eso si no vas a configurar nada, de cualquiera manera, dentro del servidor puedes seguir configurando tu Minecraft.
            </ParLeft>
            <ParLeft>
                <b>Paso 9:</b> Una vez dentro del servidor tendrás que registrarte y para ello deberás usar el comando: <Spam text="/register Contraseña Contraseña" />
            </ParLeft>
            <ParLeft>
            A partir de ahí, las siguientes veces que ingreses al servidor deberàs usar el comando: <Spam text="/login Contraseña" />
            </ParLeft>
            <ParLeft>
                <b>Paso 10:</b> ¡DISFRUTA! 😎 <img src="https://cdn.discordapp.com/emojis/822805054620172298.gif" className="inline-block h-5 -translate-y-1"/>.
            </ParLeft>
        </div>
    );
}
