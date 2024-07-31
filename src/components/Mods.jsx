import React, { useState, useEffect } from "react";
import TitleWiki from "./react/TitleWiki";
import ListMods from "./react/ListMods";

export default function Mods() {
    return (
        <div className="flex flex-col justify-center items-center">
            <ListMods />
        </div>
    );
}