import { useEffect, useState } from "react";
import TitleWiki from "./TitleWiki";
import ParLeft from "./ParLeft";
import Link from "./Link";
import Spam from "./Spam";
import ButtomWiki from "./ButtomWiki";
import SubTitleWiki from "./SubTitleWiki";
import HoverModWiki from "./HoverModWiki";

export default function ListMods() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [totalMods, setTotalMods] = useState(0);
    const [totalModsDependientes, setTotalModsDependientes] = useState(new Set());
    const [totalComplementos, setTotalComplementos] = useState(0);
    const [totalComplementosDependientes, setTotalComplementosDependientes] = useState(new Set());
    const [totalModsComplementos, setTotalModsComplementos] = useState(0);

    useEffect(() => {
        fetch('https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al obtener los datos de la API');
                }
                return response.json();
            })
            .then(data => {
                let modsCount = 0;
                let modsDependientes = new Set();
                let complementosCount = 0;
                let complementosDependientes = new Set();

                data.mods.forEach(mod => {
                    if (mod.disponible) {
                        modsCount++;
                        if (mod.dependencia && mod.dependencia.length > 0) {
                            mod.dependencia.forEach(dependencia => {
                                modsDependientes.add(dependencia.name);
                            })
                        }
                    }
                })
                data.complementos.forEach(complemento => {
                    if (complemento.disponible) {
                        complementosCount++;
                        if (complemento.dependencia && complemento.dependencia.length > 0) {
                            complemento.dependencia.forEach(dependencia => {
                                complementosDependientes.add(dependencia.name);
                                if (dependencia.dependencia && dependencia.dependencia.length > 0) {
                                    dependencia.dependencia.forEach(dependencia2 => {
                                        complementosDependientes.add(dependencia2.name);
                                    })
                                }
                            })
                        }
                    }
                })
                setTotalMods(modsCount);
                setTotalModsDependientes(modsDependientes);
                setTotalComplementos(complementosCount);
                setTotalComplementosDependientes(complementosDependientes);
                setTotalModsComplementos(modsCount + modsDependientes.size);

                setData(data);
                setLoading(false);
            })
            .catch(error => console.error(error));
                setError(error);
                setLoading(false);
    }, []);

    const buildTree = (data) => {
        const textTitle = `Mods ${totalMods} + ${totalModsDependientes.size}`;
        const totalM = totalMods + totalModsDependientes.size;
        const textComplementos = `Complementos ${totalComplementos} + ${totalComplementosDependientes.size}`;
        const totalC = totalComplementos + totalComplementosDependientes.size;
        return (
            <div>
                <div className="flex justify-center">
                    <Spam text={`Kailand V ${data.configVersion} | Launcher v ${data.launcherVersion}`} />
                </div>
                {buildBranch(textTitle, data.mods, totalM)}
                {buildBranch(textComplementos, data.complementos, totalC)}
            </div>
        );
    }
    const buildBranch = (title, data, num) => {
        return (
            <div>
                    <SubTitleWiki text={title} />
                <b className="text-gray-300/50">Total: {num} Mods</b>
                <ul className="translate-x-4">
                    {
                        data
                            .filter(mod => mod.disponible)
                            .sort((a, b) => a.name.localeCompare(b.name))
                            .map(data => (
                                <li key={data.name} className="list-disc text-left w-full">
                                    <HoverModWiki name={data.name} href={data.doct} disponible={data.disponible} description={data.descripcion} file={data.file} />
                                    {data.dependencia && data.dependencia.length > 0 && (
                                        <ul className="flex flex-col ml-4">
                                            {data.dependencia.map(dependencia => (
                                                <li key={dependencia.name}>
                                                    <HoverModWiki href={dependencia.doct} name={dependencia.name} disponible={dependencia.disponible} description={dependencia.descripcion} file={dependencia.file} />
                                                </li>
                                            ))}
                                        </ul>
                                    )}
                                </li>
                            ))
                    }
                </ul>
            </div>
        )
    }
    if (loading) {
        return (
            <p>Loading...</p>
        )
    }
    if (error) {
        return (
            <p>Error: {error}</p>
        )
    }
    return (
        <div className="w-full mb-20">
            <div className="w-full justify-center flex">
                <TitleWiki text="Lista de Mods" />
            </div>
            {data && buildTree(data)}
        </div>
    )
}