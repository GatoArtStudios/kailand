export default function ButtomWiki({ text, onClick }) {
    return (
        <button onClick={onClick} className="w-11/12 text-white no-underline font-bold rounded-xl text-center mb-2 py-1 backdrop-blur-md bg-black/30 hover:bg-black/50 hover:translate-x-1">
            {text}
        </button>
    );
};