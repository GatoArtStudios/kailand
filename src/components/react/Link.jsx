export default function Link({ href, text }) {

    if (!href) {
        return (
            <span className="no-decorect text-blue-100 font-semibold hover:text-red-300">
                {text}
            </span>
        )
    }


    return (
        <a href={href} target="_blank" className="no-decorect text-blue-300 font-semibold hover:text-blue-500">
            {text}
        </a>
    );
}