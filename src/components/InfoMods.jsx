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
import FuriaInfernal from "../assets/img/FuriaInfernal.png";
import PicoMistico from "../assets/img/PicoMistico.png";
import VaritaSkull from "../assets/img/staffecho.png";
import CascoWarden from "../assets/img/wardencasco.png";
import PecheraWarden from "../assets/img/warden_chestplate.png";
import PantalonesWarden from "../assets/img/warden_leggings.png";
import BotasWarden from "../assets/img/warden_boots.png";
import BotasAgiles from "../assets/img/Botas_Agiles.png";
import GemaHelada from "../assets/img/blue_gem.png";
import GemaMistica from "../assets/img/gemakailand.png";
import Prisma from "../assets/img/bens_new_bliss_smp_gem_for_waternetwork.png";
import VenasWarden from "../assets/img/VenasWarden.png";
import CorazonWarden from "../assets/img/heart_of_the_warden.png";
import EsenciaRagnarok from "../assets/img/bolt_essence.png";
import BloqueVelox from "../assets/img/block_velox.png";
import MineralMistico from "../assets/img/mistic_ore.png";
import Negrilla from "./react/Negrilla";
import CardImg from "./react/CardImg";
import BurcherCraftCuchillo from "../assets/img/Burcher_Craft_Cuchillo.png";
import LunaRoja from "../assets/img/LunaRoja.png";
import SuperLunaRoja from "../assets/img/SuperLunaRoja.png";
import LunaAzul from "../assets/img/LunaAzul.png";
import SuperLunaAzul from "../assets/img/SuperLunaAzul.png";
import LunaCosechadora from "../assets/img/LunaCosechadora.png";
import SuperLunaCosechadora from "../assets/img/SuperLunaCosechadora.png";
import Plasmo1 from "../assets/img/Plasmo1.png";
import Plasmo2 from "../assets/img/Plasmo2.png";
import Plasmo3 from "../assets/img/Plasmo3.png";
import Plasmo4 from "../assets/img/Plasmo4.png";
import Plasmo5 from "../assets/img/Plasmo5.png";
import Plasmo6 from "../assets/img/Plasmo6.png";
import Plasmo7 from "../assets/img/Plasmo7.png";
import Plasmo8 from "../assets/img/Plasmo8.png";
import Plasmo9 from "../assets/img/Plasmo9.png";
import Plasmo10 from "../assets/img/Plasmo10.png";
import Plasmo11 from "../assets/img/Plasmo11.png";
import Plasmo12 from "../assets/img/Plasmo12.png";
import ButcherCraftgan from "../assets/img/ButchetCraftGan.png";

export default function InfoMods() {
    return (
        <div className="flex flex-col justify-center items-center w-full">
            <TitleWiki text="Mod Pack de Kailand" />
            <div id="kailand_mod"></div>
            <SubTitleWiki text="Kailand Mod" />
            <ParLeft>
                Es un mod de Kailand V creado para el servidor y la temática del mismo, en el cual contiene muchos ítems variados, 
                desde armaduras hasta armas de combate con habilidades especiales de larga y corta distancia, entre muchos otros. A 
                continuación, te voy a explicar, ¿Cuáles son? ¿Para qué sirven?, ¿Cómo se craftean o cómo se consiguen?:
            </ParLeft>
            <SubTitleWiki text="Economía 💵" />
            <div id="economia"></div>
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
            <CardItem itemSrc={FuriaInfernal.src}>
                <Spam text="Furia infernal:"/> Forjada por los primogénitos del Ignis. Esta formidable arma con un simple clic derecho, convoca una pared ardiente con una explosión (que no daña ningún bloque) a los enemigos que se encuentran delante del portador cada 35 segundos, quitándoles vida y empujándolos. Además, la <Negrilla text="Furia infernal"/> tiene 18.5 de <Negrilla text="daño"/>, 1 de <Negrilla text="velocidad de ataque"/> y 2300 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={PicoMistico.src}>
                <Spam text="Pico místico:"/> Es una herramienta con una receta (de mejora) creada por los Dioses de <Negrilla text="Kailand"/>, está a disposición de cualquier usuario que encuentre una <Negrilla text="Gema mística"/> y tenga un <Negrilla text="pico de Netherite"/>; combinándolos en una <Negrilla text="mesa de herrería"/>, da como resultado el <Negrilla text="Pico Místico"/>. Este pico tiene el poder mágico de desatar el fuego interno de los minerales, fundiéndolos al instante con cada golpe. Además, el <Negrilla text="Pico Místico"/> tiene 20 de <Negrilla text="eficiencia"/> por defecto, nivel 4 de <Negrilla text="Romper"/> (esto quiere decir que es capaz de picar prácticamente cualquier bloque) y tiene <Negrilla text="3500 de durabilidad"/>.
            </CardItem>
            <CardItem itemSrc={VaritaSkull.src}>
                <Spam text="Varita de Skull:"/> Forjada con las cuerdas vocales de los Wardens antiguos, esta, tiene el poder de canalizar esa energía de grito que ellos utilizan para, lanzar un rayo super sónico que atraviesa cualquier bloque; a una distancia máxima de 18 bloques. Además, la <Negrilla text="Varita de Skull"/> tiene un daño mágico (anulando la armadura) de <Negrilla text="3 corazones"/>, ocasionando un efecto de <Negrilla text="Oscuridad 5"/> durante <Negrilla text="5 segundos"/> y con un <Negrilla text="cooldown de 7 segundos"/> por rayo. <Negrilla text="Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <div id="armaduras"></div>
            <SubTitleWiki text="Armaduras 🔰"/>
            <CardItem itemSrc={CascoWarden.src}>
                <Spam text="Casco de Warden:"/> Parte de la <Negrilla text="Armadura de Warden,"/> este se obtiene, teniendo un <Negrilla text="casco de Netherite"/> y un <Negrilla text="Corazón de Warden"/>; en una <Negrilla text="mesa de herrería"/>, los combinas y 
                obtendrás el <Negrilla text="Casco de Warden"/>. Además de ser indestructible, el <Negrilla text="Casco de Warden"/> tiene 8 de <Negrilla text="armadura"/>, 10 de <Negrilla text="dureza de armadura"/>, 6 de <Negrilla text="resistencia al empuje"/>, otorga <Negrilla text="apnea 2"/> 
                infinita y una enorme <Negrilla text="protección contra la infección"/> de los zombies.
            </CardItem>
            <CardItem itemSrc={PecheraWarden.src}>
                <Spam text="Pechera de Warden:"/> Parte de la <Negrilla text="Armadura de Warden"/>, este se obtiene, teniendo una <Negrilla text="pechera de Netherite"/> y un <Negrilla text="Corazón de Warden"/>; 
                en una <Negrilla text="mesa de herrería"/>, los combinas y obtendrás el <Negrilla text="Casco de Warden"/>. Además de ser indestructible, la <Negrilla text="Pechera de Warden"/> tiene 11 de <Negrilla text="armadura"/>, 
                10 de <Negrilla text="dureza de armadura"/>, 6 de <Negrilla text="resistencia al empuje"/>, otorga <Negrilla text="fuerza"/> 1 infinita y una enorme <Negrilla text="protección contra la infección"/> de los zombies.
            </CardItem>
            <CardItem itemSrc={PantalonesWarden.src}>
                <Spam text="Pantalones de Warden:"/> Parte de la <Negrilla text="Armadura de Warden"/>, este se obtiene, teniendo un <Negrilla text="pantalón de Netherite"/> 
                y un <Negrilla text="Corazón de Warden"/>; en una <Negrilla text="mesa de herrería"/>, los combinas y obtendrás el <Negrilla text="pantalón de Warden"/>. Además de ser indestructible, 
                el <Negrilla text="pantalón de Warden"/> tiene 9 de <Negrilla text="armadura"/>, 10 de <Negrilla text="dureza de armadura"/>, 6 de <Negrilla text="resistencia al empuje"/>, otorga <Negrilla text="velocidad 1"/> infinita y 
                una enorme <Negrilla text="protección contra la infección"/> de los zombies.
            </CardItem>
            <CardItem itemSrc={BotasWarden.src}>
                <Spam text="Botas de Warden:"/> Parte de la <Negrilla text="Armadura de Warden"/>, este se obtiene, teniendo unas <Negrilla text="botas de Netherite"/> y un <Negrilla text="Corazón de Warden"/>; 
                en una <Negrilla text="mesa de herrería"/>, los combinas y obtendrás las <Negrilla text="botas de Warden"/>. Además de ser indestructible, las <Negrilla text="botas de warden"/> tienen 7 de 
                <Negrilla text="armadura"/>, 10 de <Negrilla text="dureza de armadura"/>, 6 de <Negrilla text="resistencia al empuje"/> y una enorme<Negrilla text=" protección contra la infección"/> de los zombies.
            </CardItem>
            <CardItem itemSrc={BotasAgiles.src}>
                <Spam text="Botas ágiles:"/> Son botas con vida propia que tienen alas, las cuales te permiten saltar dos veces. Además, 
                las <Negrilla text="Botas ágiles"/> tienen <Negrilla text="velocidad 1"/> infinita, <Negrilla text="gracia de delfín 2"/>, 4 de <Negrilla text="armadura"/>, 10 de <Negrilla text="dureza de armadura"/>, 1 <Negrilla text="resistencia 
                al empuje"/> y 325 de <Negrilla text="durabilidad. Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <div id="piedras_preciosas"></div>
            <SubTitleWiki text="Piedras preciosas 💎"/>
            <CardItem itemSrc={GemaHelada.src}>
                <Spam text="Gema helada:"/> Es una piedra de hielo creado por un antiguo espíritu de los glaciares de la Antártida. 
                Además, la <Negrilla text="Gema helada"/> es capaz de <Negrilla text="congelar"/> a cualquier enemigo en un rango de 3x3 a la redonda, dándoles <Negrilla text="lentitud"/> 15 
                (este efecto dura 9 segundos), <Negrilla text="luminosidad"/> 1 (este efecto dura 10 segundos). <Negrilla text="Esta se obtiene comprándola en la tienda. 
                Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={GemaMistica.src}>
                <Spam text="Gema mística:"/> Es una piedra preciosa resguardada por el <Negrilla text="Dragon del End"/> que se encuentra en las 
                profundidades de sus islas, con una probabilidad mucho menor que los <Negrilla text="escombros de Netherite"/>. Dentro de ella alberga 
                un <Negrilla text="Enderman"/> con un gran poder y velocidad de teletransportación, teletransportando los bloques de su isla para formar 
                una pared temporal (que dura 30 segundos) de 3x4 y así proteger a su portador de cualquier ataque. Además, la <Negrilla text="Gema 
                mística"/> tiene un <Negrilla text="cooldown"/> de 45 segundos para poner otra pared. 
            </CardItem>
            <CardItem itemSrc={Prisma.src}>
                <Spam text="Prisma:"/> Es una piedra mágica de los antiguos Dioses de <Negrilla text="KAILAND"/>. Esta se obtiene, poniendo 
                4 <Negrilla text="Gemas místicas"/>, 4 <Negrilla text="bloques de Netherite"/> y 1 <Negrilla text="estrella del Nether"/> en una mesa de crafteo, lo que da como 
                resultado el <Negrilla text="Prisma"/>. El <Negrilla text="Prisma"/> al ser activado, te permite ser inmune a cualquier tipo de daño (Inmortalidad) 
                durante 5 segundos, con un <Negrilla text="cooldown"/> de 15 segundos.
            </CardItem>
            <div id="fragmentos_minerales"></div>
            <SubTitleWiki text="Fragmentos y minerales ☄️"/>
            <CardItem itemSrc={VenasWarden.src}>
                <Spam text="Venas de Warden:"/> Estas se obtienen matando a un <Negrilla text="Warden"/> (solo dropea 1 por <Negrilla text="Warden"/>). 
            </CardItem>
            <CardItem itemSrc={CorazonWarden.src}>
                <Spam text="Corazón de Warden:"/> Este se obtiene, poniendo 9 <Negrilla text="venas de Warden"/> en una mesa de crafteo, lo cual 
                da como resultado el <Negrilla text="Corazón de Warden"/>. Este sirve para mejorar tu <Negrilla text="armadura de Netherite"/> a la <Negrilla text="armadura de Warden"/>.
            </CardItem>
            <CardItem itemSrc={EsenciaRagnarok.src}>
                <Spam text="Esencia de Ragnarök:"/> Es una esencia mágica que alberga mucho poder. <Negrilla text="Esta se obtiene comprándola en la tienda"/>.
            </CardItem>
            <CardItem itemSrc={BloqueVelox.src}>
                <Spam text="Bloque velox:"/> Muy similar a la <Negrilla text="Piedra"/> del Minecraft Vanilla, pero más azulada. 
                Este bloque se encuentra en el Overworld a una altura no tan profunda. El <Negrilla text="Bloque Velox"/> tiene 
                la propiedad <Negrilla text="mágica de acelerar"/> el paso de cualquier entidad al caminar o correr sobre el mismo.
            </CardItem>
            <CardItem itemSrc={MineralMistico.src}>
                <Spam text="Mineral místico:"/> El tesoro más preciado del Dragón del End. Se genera dentro de las islas del End con mucho menos probabilidad que la Esmeralda y los Escombros de Netherite. 
            </CardItem>
            <div id="kailand_finder"></div>
            <SubTitleWiki text="Kailand Finder 🔎"/>
            <ParLeft>
                Es un mod que tiene una única y simple utilidad, buscar y encontrar cualquier bloque en el mundo. Al momento de poner el comando:
                <br></br>
                    <br></br>
            <Spam text="/tellme locate block to-chat simple all-loaded-chunks"/> `ID del Bloque`
                <br></br>
                    <br></br>
                        Este te mostrará las coordenadas del bloque en concreto y muchas otras funciones que tiene el mod. 
            </ParLeft>
            <div id="butcher_delight"></div>
            <SubTitleWiki text="Butcher Delight 🍗"/>
            <ParLeft>
                Consiste en un mod que implementa mecánicas que te permiten obtener una mayor cantidad de comida 
                provenientes de animales y otras cosas como, cuero e hilo de una forma un poco más realista, pero 
                un poco más difícil. Al asesinar a un animal notarás que te dará su cadáver y su comida directa. 
                Necesitarás hacer el <Negrilla text="“Cuchillo de carnicero”"/> o <Negrilla text="“Cleaver”"/> (se hace con 1 de hierro, 1 pepito de hierro y 1 palo) 
                para poder extraer comida de los animales. Si tienes el <Negrilla text="Cuchillo de carnicero"/> y colocas el cuerpo 
                del animal en el suelo y le extraes la carne, no obtendrás tanta cantidad como si lo hicieras con 
                el <Negrilla text="“Gancho de carne”"/> o <Negrilla text="“Meat hook”"/>. El <Negrilla text="“gancho de carne”"/> te permitirá colgar los cuerpos de los 
                animales para que, cuando les extraigas la carne, te de una mayor cantidad de comida. 
            </ParLeft>
            <div className="grid grid-cols-2">
                <CardImg ImgSrc={BurcherCraftCuchillo.src} heightImg="200px" />
                <CardImg ImgSrc={ButcherCraftgan.src} heightImg="200px" />
            </div>
            <div id="enhanced_celestials"></div>
            <SubTitleWiki text="Enhanced Celestials 🌟"/>
            <ParLeft>
                Es un gran mod que agrega una probabilidad de que aparezca una luna distinta en la noche. No siempre estará la luna que todos conocemos. Este mod agrega tres tipos más de luna:
            </ParLeft>
            <div className="justify-start w-full">
                <ul>
                    <li className="list-disc ml-5">
                        <Spam text="Luna sangrienta:"/> Multiplica la aparición de los mobs hostiles <Negrilla text="x2,25"/>. Con una Probabilidad de <Negrilla text="0,1 (10%)"/>.
                        <div className="w-96">
                            <CardImg ImgSrc={LunaRoja.src} heightImg="200px" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Super luna sangrienta:"/> Multiplica la aparición de los mobs hostiles <Negrilla text="x4,5"/>. Con una Probabilidad de <Negrilla text="0,05 (5%)"/>.
                        <div className="w-96">
                            <CardImg ImgSrc={SuperLunaRoja.src} heightImg="200px" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Luna azul:"/> Efecto de <Negrilla text="suerte 1"/> a todos los jugadores en el Overworld. Con una probabilidad de <Negrilla text="0,1 (10%)"/>.
                        <div className="w-96">
                            <CardImg ImgSrc={LunaAzul.src} heightImg="200px" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Super luna azul:"/> Efecto de <Negrilla text="suerte 4"/> a todos los jugadores en el Overworld. Con una probabilidad de <Negrilla text="0,05 (5%)"/>.
                        <div className="w-96">
                            <CardImg ImgSrc={SuperLunaAzul.src} heightImg="200px" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Luna cosechadora:"/> Multiplica <Negrilla text="x2"/> las cosechas que se pueden obtener. Con una probabilidad de <Negrilla text="0,1 (10%"/>).
                        <div className="w-96">
                            <CardImg ImgSrc={LunaCosechadora.src} heightImg="200px" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Super luna cosechadora:"/> Multiplica <Negrilla text="x4"/> las cosechas que se pueden obtener. Con una probabilidad de <Negrilla text="0,05 (5%)"/>.
                        <div className="w-96">
                            <CardImg ImgSrc={SuperLunaCosechadora.src} heightImg="200px" />
                        </div>
                    </li>
                </ul>
            </div>
            <div id="parcool"></div>
            <SubTitleWiki text="Parcool 🏃‍♂️"/>
            <ParLeft>
                Es un Mod de movilidad que te ayudará a ser más ágil al momento de moverte. Puedes hacer muchas cosas: trepar muros, esprintar, deslizarte por el suelo, saltar y correr entre paredes, deslizarte en paredes, dashea, voltereta y mucho más.
            </ParLeft>
            <div className="justify-start w-full">
                <ul>
                    <li className="list-disc ml-5">
                        <Spam text="Breakfall / cancelar caída:"/> Permite reducir el daño por caída, haciendo un giro justo antes de tocar el suelo.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Cling to Cliff / agarrarse del borde:"/> Permite agarrarse de un borde de un bloque y trepar alturas de hasta de tres bloques.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Crawl / arrastrarse:"/> Puedes colocarte cuerpo a tierra, permitiéndote acceder a espacios de 1x1 bloques.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Dodge / esquivar:"/> Permite realizar un rápido movimiento hacia cualquier lado (un dash) para esquivar ataques.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Run / sprintar:"/> Permite correr más rápido.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Flip / salto volterete:"/> Permite hacer una vuelta en el aire.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Hang Down / colgarse:"/> Permite trepar por bloques como cadenas, varas de end, vallas, etc.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Horizontal Wall-Run:"/> Mientras esprintas, te permite correr por las paredes por un corto período de tiempo.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Quick turn / Giro rápido:"/> Permite darte vuelta rápida.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Vault / Saltar obstáculo:"/> Mientras esprintas, puedes saltar obstáculos rápidamente.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Wall Jump / Salto de pared:"/> Mientras haces un Wall slide, tienes la capacidad de saltar hacia otra dirección.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Wall Slide / Deslizase por la pared:"/> Permite que puedas agarrarte de una pared y caer más lento y evitar el daño de caída.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Enable parcool / activar parcool:"/> Si tienes algún tipo de molestia, puedes desactivar las funciones del mod.
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Open Settings / abrir opciones:"/> Puedes abrir las configuraciones del mod.
                    </li>
                </ul>
            </div>
            <div id="enhanced_ia"></div>
            <SubTitleWiki text="Enhanced IA 👾"/>
            <ParLeft>
                Es un Mod que <Negrilla text="modifica la inteligencia"/> de todos los mobs enemigos y algunos otros más, para que 
                posean comportamientos notablemente diferentes y más difíciles: <Negrilla text="zombies, creeper, esqueletos, arañas, brujas, endermans, blazes, silverfish, etc."/> 
                Por ejemplo, hay probabilidades de que aparezcan <Negrilla text="zombies con caña de pescar"/> 
                (te engancha y te atrae hacia él) o una <Negrilla text="perla de ender"/> (la lanza y se teletransporta hacia a ti o lo más cerca de ti posible) 
                y los demás mobs también tienen otras habilidades. Cabe destacar, que la gran mayoría de mobs están personalizados 
                y están configurados para <Negrilla text="ser más difíciles de lo normal"/>.
            </ParLeft>
            <div id="the_hordes"></div>
            <SubTitleWiki text="The hordes 🧟"/>
            <ParLeft>
                Es un mod que agrega <Negrilla text="características apocalípticas y modifica el comportamiento de algunos mobs hostiles. 
                La infección"/>, sin lugar a duda es lo que destaca de este mod. Puedes contraer la infección si <Negrilla text="un zombie 
                te golpea"/> (esto no pasa siempre, hay una mediana posibilidad que te infecte, pero de cualquier manera 
                tienes maneras de evitar la infección) y una vez infectado, la <Negrilla text="infección avanzará progresivamente"/> y 
                notarás algunos síntomas. Además, si mueres estando infectado, dejaras en tu lugar de muerte un <Negrilla text="zombie 
                con tu skin, nombre y con todas tus cosas"/>, para recuperarlas deberás matarlo. Cada armadura de Minecraft Vanilla 
                y algunas de mods, poseen un <Negrilla text="porcentaje de protección contra la infección"/>. Es decir que, si un zombie te golpea, 
                la probabilidad de infección va a ser reducida dependiendo de la armadura que lleves y del porcentaje total que 
                acumules (en caso que uses extremidades diferentes de armaduras). Otra cosa muy importante, es que habrá <Negrilla text="hordas"/>; 
                cada determinado tiempo y durante la noche, es posible que aparezca una gran horda de zombies <Negrilla text="cerca"/> tuya.
            </ParLeft>
            <div id="plasmo"></div>
            <SubTitleWiki text="Plasmo 🎤"/>
            <ParLeft>
                Es un mod de chat de voz muy completo y con múltiples opciones de configuraciones. A continuación, te voy a explicar las más importantes y las que te recomendamos que configures: 
            </ParLeft>
            <div className="justify-start w-full">
                <ul>
                    <li className="list-disc ml-5">
                        <Spam text="Activation threshold / Umbral de activación:"/> Permite configurar lo fuerte que debe ser los sonidos de tu micrófono para que sea detectado. Sirve como una <Negrilla text="especie de filtro"/>, por si posees algún ruido de fondo. Mientras <Negrilla text="más bajo lo tengas, más se te va a escuchar, y mientras más alto, más fuerte deberán ser los sonidos para que sean detectados"/> tanto como tu voz, como cualquier otro ruido de fondo que tengas al tu alrededor.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo1.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Microphone / Micrófono:"/> Permite escoger el micrófono que usarás para hablar.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo2.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Microphone volumen / Volumen del micrófono:"/> Permite configurar el volumen de tu micrófono.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo3.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Noise suppression / Supresión de ruido:"/> Permite activar un filtro de supresión de ruidos.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo4.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Stereo capture / Captura estéreo:"/> Crea una <Negrilla text="sensación de dirección"/> y espacio en la grabación, lo que hace que el sonido parezca más <Negrilla text="tridimensional y realista"/>.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo5.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Output device / Dispositivo de salida:"/> <Negrilla text="Permite seleccionar"/> el dispositivo de salida, es decir, <Negrilla text="en qué dispositivo vas a escuchar las voces de los demás"/> (puede ser un auricular, parlante, etc). Si no escuchas a los demás, debes revisar esto y escoger el correcto.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo6.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Volume / Volumen del dispositivo de salida:"/> Permite configurar que tan fuerte quieres escuchar a los demás jugadores.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo7.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Proximity / Procimidad:"/> Permite configurar el volumen de todos los usuarios al mismo tiempo.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo8.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Activation type / Tipo de activación:"/> Esta opción tiene la funcionalidad de escoger 2 alternativas. La primera (y la que viene por predeterminado) <Negrilla text="&quot;Push-to-talk&quot;"/> o <Negrilla text="&quot;pulsar para hablar&quot;"/>, como su nombre indica, el jugador tendrá que <Negrilla text="presionar"/> una tecla <Negrilla text="para que el micrófono se active"/> para los demás jugadores, si deja de presionar esta tecla, vas a dejar de ser escuchado por los demás, ya que tu micro se muteará. La segunda <Negrilla text="&quot;Voice&quot; o &quot;voz&quot;"/>, sirve para <Negrilla text="tener el micrófono siempre activo"/> que todos los jugadores cercanos te escuchen.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo9.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Push-to-talk Button / Botón de presionar para hablar:"/> También llamada <Negrilla text="&quot;Botón de presionar para hablar&quot;"/>, sirve para <Negrilla text="seleccionar la tecla de preferencia"/> del jugador <Negrilla text="para que al mantenerla"/> pulsada te <Negrilla text="permita hablar"/>, al dejar de pulsarla, rápidamente te mutearás (Esto solo pasa si escoges la opción <Negrilla text="&quot;Push-to-talk&quot;"/> o <Negrilla text="&quot;pulsar para hablar&quot;"/>). 
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo10.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Proximity distance / Distancia de proximidad:"/> Esta opción te permite escoger la distancia de bloques en el cuál un jugador quiere que sea escuchado.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo11.src} heightImg="h-auto" />
                        </div>
                    </li>
                    <li className="list-disc ml-5">
                        <Spam text="Mute microphone / Silenciar micrófono:"/> También llamada <Negrilla text="&quot;Mutear micrófono&quot;"/>, en esta opción <Negrilla text="el usuario escoge la tecla para mutearse"/> (La tecla &quot;M&quot; viene escogida por predeterminado). Es <Negrilla text="recomendable usarlo si eliges la opción &quot;Voice&quot;"/> o <Negrilla text="&quot;Voz&quot;"/> en el apartado de <Negrilla text="&quot;Activación&quot;"/>, para así tener un atajo de teclado para mutearse.
                        <div className="h-max-[300px]">
                            <CardImg ImgSrc={Plasmo12.src} heightImg="h-auto" />
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    )
}
