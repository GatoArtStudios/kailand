import TitleWiki from "./react/TitleWiki";
import ParCenter from "./react/ParCenter";
import ParLeft from "./react/ParLeft";
import Link from "./react/Link";
import Nota from "./react/Nota";

export default function Ingreso() {
    return (
        <div className="flex flex-col justify-center items-center">
            <TitleWiki text="Guía de Ingreso" />
            <ParCenter>
            ¡Si tienes pensado ingresar al server, por favor, léete todas las Reglas del Servidor para evitar futuras sanciones y malentendidos!
            </ParCenter>
            <ParLeft>
                <b>Paso 1:</b> Entra a nuestro servidor de <Link href="https://kailand.es/discord" text="Discord" /> o ingresa a nuestra <Link href="https://kailand.es" text="página web." />
            </ParLeft>
            <ParLeft>
                <b>Paso 2:</b> Descarga el <Link href="https://kailand.es/downloads" text="Launcher" /> que se encuentra en la parte superior" de KAILAND V. OJO, no requiere ninguna instalación de Java, ni de ninguna versión de Forge.
            </ParLeft>
            <ParLeft>
                <b>Paso 3:</b> Escoge la versión de tu sistema operativo. Para Windows es recomendado el <b>“Instalador”</b>.
            </ParLeft>
            <Nota>
            Si por casualidad de la vida porque eres medio pendejo descargaste el que dice “comprimido” y no sabes para qué sirve, ni que hacer después, ¡NO TE PREOCUPES! Estàs solo. Por lo que deberías ir a checarte con un psicólogo y luego solo tienes que seleccionar la opción que dice “Extraer aquí” y ya tendrás el ejecutable ;D.
            </Nota>
            <ParLeft>
                <b>Paso 4:</b> Abre o ejecuta el Launcher e instala los recursos necesarios que te pide (Estos recursos son: Mods, Java, configuraciones, Forge, entre otros).
            </ParLeft>
            <ParLeft>
                <b>Paso 5:</b> Seleccionas el apartado de “Perfil”. Escoges tu tipo de cuenta y clickeas “Offline” (Solo disponible por el momento). Después, escribes tu nombre de usuario (También puedes colocar el nombre de tu cuenta Premiun si deseas). Posteriormente, le das a “Guardar”.
            </ParLeft>
            <ParLeft>
                <b>Paso 6:</b> Seleccionas el apartado de “Mods” y podrás escoger los mods de tu preferencia. Te recomendamos dejar activado y activar los de rendimiento (No importa si tienes una PC con buenos componentes), en la sección de “Predeterminados”: Rubidium, FPS Reducer, Better FPS, y en la sección de “Recomendados”: Rubidium Extras. Cabe recalcar que, cuando desactivas cualquier opción, automáticamente se elimina el archivo, y si lo vuelves a activar se descargar nuevamente.
            </ParLeft>
            <ParLeft>
                <b>Paso 7:</b> Dirígete al apartado de “Ajustes” y selecciona la mitad de la memoria RAM de la cantidad total que te muestra el Launcher, ya que él mismo se encarga de detectar cuánta memoria RAM tienes disponible en tu computador. Cabe aclarar que, no es necesario poner más de 10Gb de memoria RAM con configuraciones medias en el juego. 
            </ParLeft>
            <ParLeft>
                <b>Paso 8:</b> Clickea el botón de “Jugar” del Launcher y dentro del Juego. Eso si no vas a configurar nada, de cualquiera manera, dentro del servidor puedes seguir configurando tu Minecraft.
            </ParLeft>
            <ParLeft>
                <b>Paso 9:</b> Una vez dentro del servidor tendrás que registrarte y para ello deberás usar el comando: /register Contraseña Contraseña
            </ParLeft>
            <ParLeft>
            A partir de ahí, las siguientes veces que ingreses al servidor deberàs usar el comando: /login Contraseña
            </ParLeft>
        </div>
    );
}