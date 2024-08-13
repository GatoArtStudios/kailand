import SubTitleWiki from "./react/SubTitleWiki";
import TitleWiki from "./react/TitleWiki";
import ParLeft from "./react/ParLeft";
import CardItem from "./react/CardItem";
import Spam from "./react/Spam";
import MonedaRota from "../assets/img/coin_rota.png";
import Moneda from "../assets/img/coin.png";
import MonedaPurple from "../assets/img/coin_purple.png";
import MonedaRed from "../assets/img/coin_red.png";
import HachaNordica from "../assets/img/diamond_viking_axe.png";
import HachaLeviatan from "../assets/img/leviathan_kratos_axe_in_god_of_war.png";
import Katana from "../assets/img/katanita.png";
import Tsuke from "../assets/img/katana.png";
import Cuchilla from "../assets/img/attack_on_titan_sword.png"
import Mjolnir from "../assets/img/mjonlirlanzar.png";
import EspadaVampirica from "../assets/img/vampire_blade.png";
import Guadana from "../assets/img/clownpierce_s_axe_texture_pack.png";
import MazoHeroico from "../assets/img/obsidian_hammer.png";
import EspadaSonica from "../assets/img/warden_sword.png";
import Antidisturbios from "../assets/img/shiel.png";
import EspadaMistica from "../assets/img/mistsplitter_reforged.png";
import MartilloGravedad from "../assets/img/martillogravedad.png";
import EspadaShulker from "../assets/img/shulker_sword.png";
import VaraDictado from "../assets/img/voidstaff.png";
import MoonStaff from "../assets/img/moon_staff.png";
import StaffGoldenCrook from "../assets/img/staff_golden_crook.png";
import Negrilla from "./react/Negrilla";

export default function InfoMods() {
    return (
        <div className="flex flex-col justify-center items-center w-full">
            <TitleWiki text="Mod Pack de Kailand" />
            <SubTitleWiki text="Kailand Mod" />
            <ParLeft>
                Es un mod de Kailand V creado para el servidor y la temática del mismo, en el cual contiene muchos ítems variados, 
                desde armaduras hasta armas de combate con habilidades especiales de larga y corta distancia, entre muchos otros. A 
                continuación, te voy a explicar, ¿Cuáles son? ¿Para qué sirven?, ¿Cómo se craftean o cómo se consiguen?:
            </ParLeft>
            <SubTitleWiki text="Economía 💵" />
            <CardItem itemSrc={MonedaRota.src}>
            <Spam text="Moneda Rota:"/> Esta moneda se obtiene al abrir cofres generados en el mundo. Con 9 de ellas, obtendrán <b>1 Moneda de oro</b> en la tienda..
            </CardItem>
            <CardItem itemSrc={Moneda.src}>
                <Spam text="Moneda de oro:"/> Esta moneda se compra en la tienda, necesitarás <b>9 Monedas rotas</b> para obtener <b>1 Moneda de oro</b> y esta sirve para comprar ítems en la tienda.
            </CardItem>
            <CardItem itemSrc={MonedaPurple.src}>
                <Spam text="Moneda amatista:"/> Esta moneda se consigue participando en cualquier evento organizado por Kailand. Con ella podrás comprar ítems exclusivos en la tienda. Con 4 <Negrilla text="Monedas amatista"/> podrás obtener 1 <Negrilla text="Moneda Rubí"/>.
            </CardItem>
            <CardItem itemSrc={MonedaRed.src}>
                <Spam text="Moneda Rubí:"/> Esta moneda se consigue ganando cualquier evento organizado por Kailand o intercambiándola por 4 <Negrilla text="Monedas Amatistas"/>. Esta sirve para reclamar objetos muy exclusivos en la tienda.
            </CardItem>
            <SubTitleWiki text="Armas de combate ⚔️" />
            <CardItem itemSrc={HachaNordica.src}>
                <Spam text="Hacha nórdica:"/> Es un hacha de las mitologías griegas. Tiene todas las funciones de cualquier hacha del Minecraft Vanilla y muchas más, 
                ya que tiene más daño y posibilidad de mejorarla con la <Negrilla text="Esencia de Ragnarök"/>. La <Negrilla text="Hacha nórdica"/> tiene 12.5 de <Negrilla text="daño"/>, 1 de <Negrilla text="Velocidad de ataque"/> y 
                1500 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={HachaLeviatan.src}>
                <Spam text="Hacha Leviatán:"/> Es la mejora del <Negrilla text="Hacha nórdica"/>. Esta se obtiene combinando el <Negrilla text="Hacha nórdica"/> y la <Negrilla text="Esencia de Ragnarök"/> en la mesa de herrería, 
                esto da como resultado el Hacha Leviatán, cuya habilidad es proporcionar efectos positivos después de lanzar rayos a las entidades de alrededor: <Negrilla text="Fuerza 2"/> 
                (30 segundos), <Negrilla text="Absorción 2"/> (45 segundos), <Negrilla text="Regeneración 1"/> (45 segundos) y <Negrilla text="Vida mejorada 2"/> (45 segundos). Además, el <Negrilla text="Hacha Leviatán"/> tiene <Negrilla text="20 de daño"/>, 1 de 
                <Negrilla text="velocidad de ataque"/> y 2300 de <Negrilla text="durabilidad"/>.
            </CardItem>
            <CardItem itemSrc={Katana.src}>
                <Spam text="Katana:"/> Es una <Negrilla text="Katana"/> del antiguo Japón que fue forjada con la bendición de Fujin, el dios del viento. Esta <Negrilla text="Katana"/> te permite utilizar 
                un dash (impulso) hacia adelante cada 3 segundos, permitiéndote cortar todo a tu paso. Además, la <Negrilla text="Katana"/> tiene 16.4 de daño, 1.4 de <Negrilla text="Velocidad de ataque"/> 
                y 2100 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={Tsuke.src}>
                <Spam text="Tsuke:"/> Esta espada es capaz de desatar un ataque de mil golpes mágicos a todas las entidades de alrededor del portador, en un rango de 8 bloques. 
                La <Negrilla text="Tsuke"/> tiene 16 de <Negrilla text="daño"/>, 1.2 de <Negrilla text="velocidad de ataque"/> y 2100 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={Cuchilla.src}>
                <Spam text="Cuchilla:"/> Esta hoja te permite esconderte entre las sombras para tomar a tu objetivo por sorpresa y por si este intenta escapar se 
                verá obstaculizado por su potente veneno. Además, la <Negrilla text="Cuchilla"/> tiene 14 de <Negrilla text="daño"/>, 1.1 de <Negrilla text="velocidad de ataque"/> y 2300 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={Mjolnir.src}>
                <Spam text="Mjolnir:"/> Es el martillo de Thor; un arma capaz de dominar los poderes del trueno. Al lanzar el <Negrilla text="Mjolnir"/> contra sus oponentes liberará toda la ira del dios del trueno. Además, el <Negrilla text="Mjolnir"/> tiene 13 de <Negrilla text="daño"/>, 1.6 de <Negrilla text="velocidad de ataque"/> y 2200 de <Negrilla text="durabilidad. Este se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={EspadaVampirica.src}>
                <Spam text="Espada vampírica:"/> Es una espada con una sed insaciable por consumir la sangre y la vida de tus enemigos. Al golpear a un jugador con esta espada existe la posibilidad de reponer la vitalidad de su portador con la sangre del contrincante. Además, la <Negrilla text="Espada vampírica"/> tiene 13.5 de <Negrilla text="daño"/>, 1.5 de <Negrilla text="velocidad de ataque"/> y 2850 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={Guadana.src}>
                <Spam text="Guadaña:"/> Esta <Negrilla text="Guadaña"/> contiene el poder de los cielos y de las sombras, elevando a sus enemigos hacia los cielos y cegándolos con una oscuridad profunda. Además, la <Negrilla text="Guadaña"/> tiene 15.2 de <Negrilla text="daño"/>, 1.3 de <Negrilla text="velocidad de ataque"/> y 2100 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={MazoHeroico.src}>
                <Spam text="Mazo heroico:"/> Es un mazo nacido en las forjas sagradas de las tierras de Elyria. Su habilidad mágica llamada <Negrilla text="Efecto Heroico"/> otorga el poder de ignorar la armadura de cualquier entidad al golpearla, infligiendo un daño brutal y directo. Además, el <Negrilla text="Mazo heroico"/> tiene 16 de <Negrilla text="daño"/>, 0.8 de <Negrilla text="velocidad de ataque"/> y 3200 de <Negrilla text="durabilidad. Este se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={EspadaSonica.src}>
                <Spam text="Espada sónica:"/> Es un arma mágica creada por los antiguos artesanos de Sonoris. Su habilidad especial permite al portador lanzar un devastador rayo sónico, similar al del Warden, que atraviesa cualquier armadura y cualquier bloque. Además, la <Negrilla text="Espada sónica"/> tiene 14.8 de <Negrilla text="daño"/>, 1.4 de <Negrilla text="velocidad de ataque"/> y 2750 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={Antidisturbios.src}>
                <Spam text="Antidisturbios:"/> Es un escudo antimotines de las fuerzas policiales y militares. Su función es proteger al portador de cualquier tipo de daño, menos de alguno mágicos. Además, el <Negrilla text="Antidisturbios"/> tiene 3 segundos de cooldown de desarme (dejando al portador al descubierto por un golpe de un hacha o cualquier arma de combate que haga la misma acción) y 3200 de <Negrilla text="durabilidad. Este se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={EspadaMistica.src}>
                <Spam text="Espada mística:"/> Es una espada que fue forjada en los bosques encantados de Elaria, su habilidad tiene el poder de desatar una poderosa confusión que hace girar a todos los jugadores en un radio de 8x8 bloques. Además, la <Negrilla text="Espada mística"/> tiene 13.8 de <Negrilla text="daño"/>, 1.3 de <Negrilla text="velocidad de ataque"/> y 1850 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={MartilloGravedad.src}>
                <Spam text="Martillo de gravedad:"/> Es un martillo forjado por los enanos de Khazad, manipula la fuerza gravitatoria. Su golpe principal atrae y daña a las entidades cercanas, mientras que su golpe secundario las empuja con una fuerza irresistible. Además, el <Negrilla text="Martillo de gravedad"/> tiene 16 de <Negrilla text="daño"/>, 0.8 de <Negrilla text="velocidad de ataque"/> y 2850 de <Negrilla text="durabilidad. Este se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={EspadaShulker.src}>
                <Spam text="Espada de Shulker:"/> Es la mejora de la <Negrilla text="Espada de netherite"/> del Minecraft Vanilla. Esta se obtiene combinando la <Negrilla text="Espada de netherite"/> y el <Negrilla text="Caparazón de Shulker"/> (Que se obtiene matando a un Shulker) en la mesa de herrería, esto da como resultado la <Negrilla text="Espada de Shulker"/>. Esta, cuenta con la habilidad de lanzar el proyectil del Shulker cada 3 segundos. Además, la <Negrilla text="Espada de Shulker"/> tiene 12 de <Negrilla text="daño"/>, 1.4 de <Negrilla text="velocidad de ataque"/> y 1750 de <Negrilla text="durabilidad"/>.
            </CardItem>
            <CardItem itemSrc={VaraDictado.src}>
                <Spam text="Varita del dictado:"/> Es una varita forjada por unos sabios hechiceros de dudosa procedencia. Esta varita otorga al portador la capacidad de comandar a quienes lo rodean en un radio de 10x10 bloques cada 10 segundos. Ellos deberán obedecer las órdenes, pues de lo contrario les costará su vitalidad. Además, la <Negrilla text="Varita del dictado"/> tiene 5 de <Negrilla text="daño"/>, 1.6 de <Negrilla text="velocidad de ataque"/> y 3500 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={MoonStaff.src}>
                <Spam text="Varita lunar:"/> Forjada por Selene, la diosa de la luna. La varita se alimenta por la luz de la luna (por lo que solo funciona en la noche), es un artefacto de inmenso poder. Por otro lado, la varita tiene 2 fases/habilidades. 
                <ul>
                    <li className="list-disc ml-5">
                        Dispara un <Negrilla text="rayo luminoso"/> cada 2 segundos que hace levitar a cualquier enemigo durante 1 segundo.
                    </li>
                    <li className="list-disc ml-5">
                        Invoca un <Negrilla text="círculo curativo"/> cada 40 segundos, que otorga: regeneración 1 (20 segundos), fuerza 2 (20 segundos), velocidad 1 (20 segundos) y visión nocturna (30 segundos) a quienes se encuentren dentro de ese círculo.
                    </li>
                </ul>
                <Negrilla text="Esta se obtiene comprándola en la tienda."/> 
            </CardItem>
            <CardItem itemSrc={StaffGoldenCrook.src}>
                <Spam text="Báculo dorado:"/> Forjado por los seres más antiguos de Kailand. Este báculo alterna entre tres poderosas habilidades:
                <ul>
                    <li className="list-disc ml-5">
                        <Negrilla text="Área de Regeneración:"/> Crea un círculo curativo cada 35 segundos que da, Regeneración 2 (7 segundos) a todos aquellos que estén dentro.
                    </li>
                    <li className="list-disc ml-5">
                        <Negrilla text="Cadenas de Luz:"/> Lanza un rayo congelante cada 5 segundos (el efecto de congelamiento dura 2 segundos). 
                    </li>
                    <li className="list-disc ml-5">
                        <Negrilla text="Cambio:"/> Permite intercambiar posiciones con cualquier entidad cada 8 segundos.
                    </li>
                </ul>
                <Negrilla text="Esta se obtiene comprándola en la tienda."/> 
            </CardItem>
        </div>
    )
}
