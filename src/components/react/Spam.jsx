export default function Spam({ text }) {
    return (
        <spam className="bg-slate-700 text-gray-300 p-0 rounded-md font-semibold px-2 text-center text-[15px] select-all">
            {text}
        </spam>
    );
}