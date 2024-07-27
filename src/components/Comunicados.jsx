import TitleWiki from "./react/TitleWiki";
import ParLeft from "./react/ParLeft";
import SubTitleWiki from "./react/SubTitleWiki";

export default function Comunicados() {
    return (
        <div className="flex flex-col justify-center items-center">
            <TitleWiki text="Sobre el servidor de Minecraft" />
            <ParLeft>
                <li className="my-5">
                El servidor de Minecraft (Kailand), es un juego. Por lo tanto, las peleas, disputas y discusiones dentro del servidor, se quedan dentro del servidor. No se tolerará toxicidad ni faltas de respeto, por motivos relacionados al juego.
                </li>
                <li className="my-5">
                Se recomienda a los jugadores que, usen un teclado 100% para más comodidad, debido a que, el servidor contiene muchos mods con atajos de teclado o teclas que asignar para usar los mods.
                </li>
                <li className="my-5">
                Las personas que le digan a algún administrador, un bug, serán recompensados.
                </li>
                <li className="my-5">
                El servidor es un poco gore. Por lo tanto, no nos hacemos responsables del impacto que tenga esto en los usuarios.
                </li>
                <li className="my-5">
                Se recomienda NO utilizar Packs de Texturas que modifiquen las animaciones visuales de los jugadores: caminar, correr, agacharse, entre otros (incluidas las que se pueden ver en primera persona), porque puede haber bugs visuales con algunos mods.
                </li>
                <li className="my-5">
                Ojo, cuando te infecte un zombi (aunque sea el efecto de nivel 1), tendrás que encontrar una de las muchas curas que se implementaron: manzana dorada, manzana encantada, botella de miel, guiso de remolacha, estofado de conejo, papa venenosa, pez tropical y pez globo (También brinda efecto de inmunidad, pero durante 2 minutos). De lo contrario morirás.
                </li>
                <li className="my-5">
                Las personas que tengan cualquier tipo de pertenencias a más de la distancia establecida (10.000 bloques) del Overword, serán eliminadas. Los jugadores que encuentren esas pertenencias, se las pueden quedar. Si están o son cualquier tipo de objeto de almacenamiento reforzado o con código, pueden comunicarse con algún administrador para poder quedarse con todo el contenido dentro.
                </li>
                <li className="my-5">
                Cuando estás infectado, ten cuidado al utilizar el comando /lobby. En el lobby, no aparecen mobs debido a medidas de protección. Esto significa que si mueres estando infectado mientras estás en el lobby, perderás todo tu inventario.
                </li>
                <li className="my-5">
                Los aldeanos fueron modificados para que tengan un tradeo fijo. Quiere decir que, si el jugador le asigna un rol, ya no se podrá cambiar ni el rol asignado, ni los ítems que ofrece, solo se podrá subir de nivel.
                </li>
                <li className="my-5">
                Las personas podrán crear un equipo de máximo 4 personas con el comando “/team create 'nombre del equipo'”. Tener un equipo tiene varios beneficios, como por ejemplo: el daño entre los miembros del equipo está desactivado, nombre del equipo visible a todos los jugadores, disponibilidad administrar el team a la disposición del creador, etc.
                </li>
            </ParLeft>
        </div>
    );
}