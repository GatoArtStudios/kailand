export default function SubTitleWikiCenter({ text }) {
    return (
        <div className="group relative w-full">
            <h1 className="text-2xl font-bold mb-7 mt-7 w-full group-hover:animate-bounce text-center">
                {text}
            </h1>
        </div>
    );
}