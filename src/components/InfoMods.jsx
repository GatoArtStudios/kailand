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
import MazoHeroico from "../assets/img/acha_pascua.png";
import EspadaSonica from "../assets/img/warden_sword.png";
import Antidisturbios from "../assets/img/antidisturbios.png";
import EspadaMistica from "../assets/img/espada_mistica.png";
import MartilloGravedad from "../assets/img/acha_ender.png";
import EspadaShulker from "../assets/img/shulker_sword.png";
import VaraDictado from "../assets/img/vara_infernal.png";

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
            <Spam text="Moneda Rota:"/> Esta moneda se obtiene al abrir cofres generados en el mundo. Con 9 de ellas, podrás obtener <b>1 Moneda de oro</b>.
            </CardItem>
            <CardItem itemSrc={Moneda.src}>
                <Spam text="Moneda de oro:"/> Esta moneda se compra en la tienda, necesitarás <b>9 Monedas rotas</b> para obtener <b>1 Moneda de oro</b> y esta sirve para comprar ítems en la tienda.
            </CardItem>
            <CardItem itemSrc={MonedaPurple.src}>
                <Spam text="Moneda amatista:"/> Esta moneda se consigue participando en cualquier evento organizado por Kailand. Con ella podrás comprar ítems exclusivos en la tienda. Con 4 Monedas amatista podrás obtener 1 Moneda Rubí.
            </CardItem>
            <CardItem itemSrc={MonedaRed.src}>
                <Spam text="Moneda Rubí:"/> Esta moneda se consigue ganando cualquier evento organizado por Kailand o intercambiándola por 4 Monedas Amatistas. Esta sirve para reclamar objetos muy exclusivos en la tienda.
            </CardItem>
            <CardItem itemSrc={HachaNordica.src}>
                <Spam text="Hacha nórdica:"/> Es un hacha de las mitologías griegas. Tiene todas las funciones de cualquier hacha del Minecraft Vanilla y muchas más, ya que tiene más daño y posibilidad de mejorarla con la Esencia de Ragnarök. La Hacha nórdica tiene 12.5 de daño, 1 de velocidad de ataque y 1500 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={HachaLeviatan.src}>
                <Spam text="Hacha Leviatán:"/> Es la mejora del Hacha nórdica. Esta se obtiene combinando el Hacha nórdica y la Esencia de Ragnarök en la mesa de herrería, esto da como resultado el Hacha Leviatán, cuya habilidad es proporcionar efectos positivos después de lanzar rayos a las entidades de alrededor: Fuerza 2 (30 segundos), Absorción 2 (45 segundos), Regeneración 1(45 segundos) y Vida mejorada 2 (45 segundos). Además, el Hacha Leviatán tiene 20 de daño, 1 de velocidad de ataque y 2300 de durabilidad.
            </CardItem>
            <CardItem itemSrc={Katana.src}>
                <Spam text="Katana:"/> Es una Katana que te permite utilizar un dash (empuje) hacia adelante cada 3 segundos, permitiéndote cortar todo a tu paso. Además, la Katana tiene 16.4 de daño, 1.4 de Velocidad de ataque y 2100 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={Tsuke.src}>
                <Spam text="Tsuke:"/> Esta espada es capaz de desatar un ataque de mil golpes mágicos a todas las entidades de alrededor del portador, en un rango de 8 bloques. La Tsuke tiene 16 de daño, 1.2 de velocidad de ataque y 2100 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={Cuchilla.src}>
                <Spam text="Cuchilla:"/> Esta hoja te permite esconderte entre las sombras para tomar a tu objetivo por sorpresa y por si este intenta escapar se verá obstaculizado por su potente veneno. Además, la Cuchilla tiene 14 de daño, 1.1 de velocidad de ataque y 2300 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={Mjolnir.src}>
                <Spam text="Mjolnir:"/> Es el martillo de Thor; un arma capaz de dominar los poderes del trueno. Al lanzar el Mjolnir contra sus oponentes liberará toda su ira del dios del trueno. Además, el Mjolnir tiene 13 de daño, 1.6 de velocidad de ataque y 2200 de durabilidad. Este se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={EspadaVampirica.src}>
                <Spam text="Espada vampírica:"/> Esta es una espada con un insaciable deseo por consumir la sangre y la vida de tus enemigos. Al golpear a un jugador con esta espada existe la posibilidad de reponer la vitalidad de su portador con la sangre del enemigo.  Además, la Espada vampírica tiene 13.5 de daño, 1.5 de velocidad de ataque y 2850 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={Guadana.src}>
                <Spam text="Guadaña:"/> Esta Guadaña contiene el poder de los cielos y de las sombras, elevando a sus enemigos hacia los cielos y cegándolos con una oscuridad profunda. Además, la Guadaña tiene 15.2 de daño, 1.3 de velocidad de ataque y 2100 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={MazoHeroico.src}>
                <Spam text="Mazo heroico:"/> Es un mazo nacido en las forjas sagradas de las tierras de Elyria. Su habilidad mágica llamada Efecto Heroico otorga el poder de ignorar la armadura de cualquier entidad al golpearla, infligiendo un daño brutal y directo. Además, el Mazo heroico tiene 16 de daño, 0.8 de velocidad de ataque y 3200 de durabilidad. Este se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={EspadaSonica.src}>
                <Spam text="Espada sónica:"/> Es un arma mágica creada por los antiguos artesanos de Sonoris. Su habilidad especial permite al portador lanzar un devastador rayo sónico, similar al del Warden, que atraviesa cualquier armadura y cualquier bloque. Además, la Espada sónica tiene 14.8 de daño, 1.4 de velocidad de ataque y 2750 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={Antidisturbios.src}>
                <Spam text="Antidisturbios:"/> Es un escudo antimotines de las fuerzas policiales y militares. Su función es proteger al portador de cualquier tipo de daño, menos de alguno mágicos. Además, el Antidisturbios tiene 3 segundos de cooldown de desarme (dejando al portador al descubierto por un golpe de un hacha o cualquier arma de combate que haga la misma acción) y 3200 de durabilidad. Este se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={EspadaMistica.src}>
                <Spam text="Espada mística:"/> Es una espada que fue forjada en los bosques encantados de Elaria, su habilidad tiene el poder de desatar una poderosa confusión que hace girar a todos los jugadores en un radio de 8x8 bloques. Además, la Espada mística tiene 13.8 de daño, 1.3 de velocidad de ataque y 1850 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={MartilloGravedad.src}>
                <Spam text="Martillo de gravedad:"/> Es un martillo forjado por los enanos de Khazad, manipula la fuerza gravitatoria. Su golpe principal atrae y daña a las entidades cercanas, mientras que su golpe secundario las empuja con una fuerza irresistible. Además, el Martillo de gravedad tiene 16 de daño, 0.8 de velocidad de ataque y 2850 de durabilidad. Este se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={EspadaShulker.src}>
                <Spam text="Espada de Shulker:"/> Es un martillo forjado por los enanos de Khazad, manipula la fuerza gravitatoria. Su golpe principal atrae y daña a las entidades cercanas, mientras que su golpe secundario las empuja con una fuerza irresistible. Además, el Martillo de gravedad tiene 16 de daño, 0.8 de velocidad de ataque y 2850 de durabilidad. Este se obtiene comprándola en la tienda.
            </CardItem>
            <CardItem itemSrc={VaraDictado.src}>
                <Spam text="Varita del dictado:"/> Es una varita forjada por unos sabios hechiceros de dudosa procedencia. Esta varita otorga al portador la capacidad de comandar a quienes lo rodean en un radio de 10x10 bloques cada 10 segundos. Ellos deberán obedecer las órdenes, pues de lo contrario les costará su vitalidad. Además, la Varita del dictado tiene 5 de daño, 1.6 de velocidad de ataque y 3500 de durabilidad. Esta se obtiene comprándola en la tienda.
            </CardItem>
        </div>
    )
}