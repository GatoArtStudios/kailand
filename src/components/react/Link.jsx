export default function Link({ href, text }) {
    return (
        <a href={href} target="_blank" className="no-decorect text-blue-300 font-semibold">
            {text}
        </a>
    );
}