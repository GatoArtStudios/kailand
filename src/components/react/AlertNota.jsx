export default function AlertNota({ children }) {
    return (
        <div className="italic my-5 bg-red-100 dark:bg-red-900 border-l-4 border-red-500 dark:border-redd-700 text-red-900 dark:text-red-100 p-2 rounded-lg flex items-center transition duration-300 ease-in-out hover:bg-re-200 dark:hover:bg-re-800 transform hover:scale-105 w-full">
            <svg
                stroke="currentColor"
                viewBox="0 0 24 24"
                fill="none"
                class="h-5 w-5 flex-shrink-0 mr-2 text-re-600"
                xmlns="http://www.w3.org/2000/svg"
                >
                <path
                    d="M13 16h-1v-4h1m0-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    stroke-width="2"
                    stroke-linejoin="round"
                    stroke-linecap="round"
                ></path>
            </svg>
            <p className="text-sm font-semibold">
                Alerta: {children}
            </p>
        </div>
    );
}