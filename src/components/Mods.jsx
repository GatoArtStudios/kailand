import React, { useState, useEffect } from "react";
import ListMods from "./react/ListMods";
import InfoMods from "./InfoMods.jsx";

export default function Mods() {
    return (
        <div className="flex flex-col justify-center items-center">
            <InfoMods />
            <ListMods />
        </div>
    );
}