export default function ButtomWiki({ text, onClick }) {
    return (
        <button onClick={onClick} className="text-white no-underline mr-5 font-bold rounded-xl text-center mb-2 py-1 backdrop-blur-md bg-black/30 hover:bg-black/50">
            {text}
        </button>
    );
};