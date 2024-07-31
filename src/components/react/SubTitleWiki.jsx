export default function SubTitleWiki({ text }) {
    return (
        <div className="group relative w-full">
            <h1 className="text-2xl font-bold mb-4 mt-7 text-left w-full group-hover:animate-bounce">
                {text}
            </h1>
        </div>
    );
}