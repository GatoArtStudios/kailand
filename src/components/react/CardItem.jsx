import "../../styles/Rotate3D.css";

export default function CardItem({ children, itemSrc }) {
    const animation3D = {
        animation: "3D 1s ease-in-out infinite alternate",
        transformStyle: "preserve-3d",
        transform: "perspective(1000px) rotateX(20deg) rotateY(10deg)",
    }
    return (
        <div className="group grid grid-cols-3 gap-4 mb-3 bg-black/10 p-5 rounded-xl">
            <div className="col-span-2 col-start-0">
                {children}
            </div>
            <div className="col-end-4 col-span-1 justify-end items-center flex">
                <div className="rounded-md p-1 bg-gradient-to-tr from-blue-900 to-violet-800 group relative transition-transform ease-in-out duration-300 hover:transform hover:-translate-x-2 hover:scale-125 max-h-24 w-24">
                    <div className="bg-black/60 backdrop-blur-md rounded-md p-1 justify-center flex">
                        <img
                            className="h-20 rotate-y-infinite"
                            src={itemSrc}
                        />
                    </div>
                </div>
            </div>
        </div>
    )
}