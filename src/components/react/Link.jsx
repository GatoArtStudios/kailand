export default function Link({ href, text }) {
    return (
        <a href={href} target="_blank" className="no-decorect text-blue-300 font-semibold hover:text-blue-500">
            {text}
        </a>
    );
}