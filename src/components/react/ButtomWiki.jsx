export default function ButtomWiki({ text, onClick }) {
    return (
        <button onClick={onClick} className="w-11/12 text-white no-underline font-bold rounded-xl text-center mb-2 py-1 backdrop-blur-md bg-black/30 transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-105 hover:bg-black/50 duration-300">
            {text}
        </button>
    );
};