import TitleWiki from "./react/TitleWiki";
import ParLeft from "./react/ParLeft";
import Negrilla from "./react/Negrilla";
import ImgzPark from '../assets/img/JuegoImg.png';
import ImgGolen from '../assets/img/JuegoImg1.png';
import ImgKaiAndPark from '../assets/img/JuegoImg2.png';
import ImgAllowPlayers from '../assets/img/JuegoImg3.png';
import ImgSteve from '../assets/img/JuegoImg4.png';
import ImgLootBody from '../assets/img/JuegoImg5.png';
import ImgBodys from '../assets/img/JuegoImg6.png';
import CardImg from "./react/CardImg";
import Imgur from "../assets/img/Imgur.png";
import Imgur1 from "../assets/img/Imgur1.png";
import Imgur2 from "../assets/img/Imgur2.png";
import Imgur3 from "../assets/img/Imgur3.png";
import Imgur4 from "../assets/img/Imgur4.png";
import Imgur5 from "../assets/img/Imgur5.png";
import Imgur6 from "../assets/img/Imgur6.png";
import Imgur7 from "../assets/img/Imgur7.png";
import Imgur8 from "../assets/img/Imgur8.png";
import Imgur9 from "../assets/img/Imgur9.png";
import Spam from "./react/Spam";

export default function Juego() {
    return (
        <div className="flex flex-col justify-center items-center">
            <TitleWiki text="Juego" />
            <ul className="list-disc list-outside w-full mb-10 translate-x-5 text-green-200">
                <li>
                    El server es 24/7
                </li>
                <li>
                    Muy alta dificultad, porque se modificó la inteligencia artificial de la mayoría de los mobs/entidades, además hay que tener cuidado con los zombies ya que te pueden infectar.
                </li>
                <li>
                    El servidor un poco gore.
                </li>
                <li>
                    El máximo de personas por team es de 4 personas.
                </li>
                <li>
                    La distancia límite para vivir es de 10K bloques a la redonda del lobby en el Overworld.
                </li>
                <li>
                    El por qué jugar e intentar ganar los eventos de Kailand.
                </li>
                <li>
                    Se puede robar.
                </li>
                <li>
                    Los cuerpos quedan a disposición de cualquier jugador al morir.
                </li>
            </ul>
            <ParLeft>
                El servidor no tiene como tal un objetivo, ni un final, pero una vez inicies, deberás: sobrevivir de cualquier enemigo, 
                farmear comida y materiales, explorar estructuras y biomas de todos los mundos, craftear o conseguir los ítems más fuertes 
                y raros, y participar o intentar ganar en todos los eventos que se hagan en <Negrilla text="Kailand V"/>, ya que podrás conseguir las <Negrilla text="monedas Amatista y Rubí"/>, 
                las cuales te permitirán reclamar muchos ítems fuertes y exclusivos. Cabe aclarar que, todas las armas fueron testeadas y modificadas 
                para que una persona con ítems regularmente bajos-medianos (en daño y poder) le pueda hacer frente a un jugador que lleve mucho tiempo en 
                el servidor y que tenga ítems poderosos. 
            </ParLeft>
            <div className="flex flex-row">
                <CardImg ImgSrc={ImgzPark.src} heightImg="" wigthImg="w-[300px]" />
                <CardImg ImgSrc={ImgGolen.src} heightImg="" wigthImg="w-[455px]" />
            </div>
            <ParLeft>
                Para ser el más poderoso deberás iniciar como siempre: encontrando madera, luego piedra y poniéndote en marcha en la búsqueda de hierro y mejores minerales, además de la recolección de comida. Mientras que, exploras bastos mundos y estructuras, te proteges de los enemigos cercanos (cualquier mob o jugador que quiera hacerte daño), <Negrilla text="te construyes un refugio y escoges a las 3 futuras personas (+ tu = 4 personas)"/> que formarán parte de tu equipo (clan), también puedes ir viendo los mejores ítems de los mods y todo el contenido que te ofrece el modpack de <Negrilla text="Kailand V"/>, después tendrás que armarte con tu equipo para derrotar a los boses más fuertes y despiadados y así obtener su loot. Los eventos juegan un papel muy importante en el progreso de todos los jugadores, ya que con sus recompensas (al participar o ganar) podrán reclamar armas de combate, armaduras, piedras mágicas, etc.
            </ParLeft>
            <div className="flex flex-row">
                <CardImg ImgSrc={ImgKaiAndPark.src} heightImg="h-[250px]" wigthImg="w-auto" />
                <CardImg ImgSrc={ImgAllowPlayers.src} heightImg="h-[250px]" wigthImg="w-auto" />
            </div>
            <ParLeft>
                Ten en cuenta que, el servidor es de muy alta dificultad, porque se modificó la inteligencia artificial de la mayoría de los mobs/entidades, pero sobre todo de los zombis, ya que tienen las propiedades de: infectar (con una alta probabilidad), correr, inmunidad a la luz solar, también cuentan con aliados que poseen perlas de ender, cañas de pescar, etc. Si en algún momento un zombi te llega a infectar y mueres, tu cuerpo sin vida resucitará como un zombi con tus cosas, y para recuperarlas deberás matarlo con algo de esfuerzo. El servidor es un poco gore, ya que contiene algunos mods como: <Negrilla text="Horror elements, Zombie extreme y Butcher’t delight"/>, que modifican la jugabilidad y la experiencia de todo lo relacionado con, la supervivencia y las muertes de cualquier entidad, a la misma ves que el mod <Negrilla text="Corpse"/>, ya que cumple la funcionalidad de resguardar todas las cosas del jugador, formando un cadáver en el punto de muerte a disposición de cualquier usuario. 
            </ParLeft>
            <div className="flex flex-col items-center">
                <div className="flex flex-row">
                    <CardImg ImgSrc={ImgSteve.src} heightImg="h-[250px]" wigthImg="w-auto" />
                    <CardImg ImgSrc={ImgLootBody.src} heightImg="h-[250px]" wigthImg="w-auto" />
                </div>
                    <CardImg ImgSrc={ImgBodys.src} heightImg="h-[250px]" wigthImg="w-auto" />
            </div>
            <div id="skins"></div>
            <ParLeft>
                Es importante saber que, para ver las skins de tus compañeros o de los demás jugadores (si es que no las ves) deberás salir y volver a entrar al servidor, esto por un pequeño bug que hay con el plugin <Negrilla text="SkinsRestorer"/>. También pasa cuando algún usuario cambia de skin con los comandos:
                <br /><br /><Negrilla text="Para skins existentes:"/><br />
                <Spam text="/skin <nombre de la cuenta premium>" /><br />
                <Spam text="/skin set <nombre de la cuenta premium>" /><br /><br />
                <Negrilla text="Para skins personalizadas (únicas):"/><br />
                <Spam text="/skin <url skin>" /><br />
                <Spam text="/skin url <url skin>" /><br />
                Donde la URL debe ser el link directo de la skin. Recomendamos esta web para subir la skin 
                <a href="https://imgur.com/upload" className="text-blue-500 hover:text-blue-300"> https://imgur.com/upload</a>, ya que te da una <Negrilla text="URL"/> directa y válida para el plugin <Negrilla text="SkinRestorer"/>, 
                ahí deberás crearte una cuenta y subir tu skin personalizada. <br /><br />
                Guía para crearte una cuenta y subir tu skin personalizada al servidor de Kailand:
            </ParLeft>
            <ul>
                    <li className="list-disc ml-5">
                        <Spam text="Paso uno:"/> Clickear “New post”.
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur.src} heightImg="h-[240px]" wigthImg="w-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso dos:"/> Clickear “Sign in”.
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur1.src} heightImg="h-[400px]" wigthImg="w-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso tres:"/> Clickear “need an account” sino tienes una cuenta, si ya tiene una clickear “sign in”.
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur2.src} heightImg="h-[400px]" wigthImg="w-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso cuatro:"/> Poner toda tu información.
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur3.src} heightImg="h-[400px]" wigthImg="w-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso cinco:"/> Clickear “Choose Photo/Video”.
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur4.src} heightImg="h-[400px]" wigthImg="w-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso seis:"/> Seleccionar o arrastrar la skin que quieres importar.
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur5.src} heightImg="h-[400px]" wigthImg="w-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso siete:"/> Copiar la URL o link. 
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur6.src} heightImg="h-[400px]" wigthImg="w-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso ocho:"/> Escribir cualquiera de estos 2 comandos y luego copiar la URL: <br />
                        <Spam text="/skin <url skin>" /><br />
                        <Spam text="/skin url <url skin>" /><br />
                        <div className="h-fit w-full flex justify-center">
                            <CardImg ImgSrc={Imgur7.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Paso nueve:"/> ¡Disfruta! 😎
                        <div className="flex flex-row">
                            <div className="h-fit w-full flex justify-center">
                                <CardImg ImgSrc={Imgur8.src} heightImg="h-auto" wigthImg="w-[400px]" />
                            </div>
                            <div className="h-fit w-full flex justify-center">
                                <CardImg ImgSrc={Imgur9.src} heightImg="h-auto" wigthImg="w-[387px]" />
                            </div>
                        </div>
                    </li>
                </ul>
            <ParLeft>
                Cabe recalcar que: el servidor siempre estará prendido, ya que es 24/7. A menos que esté en mantenimiento. De cualquier manera, el equipo de staff siempre estará avisando a todos y les mantendrá al tanto en nuestro servidor de <a href="https://kailand.es/discord" className="text-blue-500 hover:text-blue-300">discord</a>, específicamente en el canal de 
                <a href="https://discord.com/channels/1074070315124138078/1086793825726509186"><Spam text="「🟨」avisos. "/></a>
            </ParLeft>
            <ParLeft>
                También tienen que saber que, es importante que todos los jugadores utilicen nuestro Launcher, ya que así podemos garantizar el disfrute de la mejor experiencia de juego y de la mayor seguridad; para evitar el abuso de los famosos hacks o conocidos cheats, los cuales dan ventajas a los jugadores que los utilizan, sobre los usuarios que no. Esto también nos permite evitar ataques de bots al servidor (lo que puede ocasionar lag o hasta un crasheo). Nos aseguramos que todos jueguen en igualdad de condiciones y sin problemas, además de ser una buena forma de representar al servidor de una manera estética. Por todas esas razones el uso del Launcher es obligatorio para Kailand V.
            </ParLeft>
        </div>
    );
}