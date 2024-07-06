# Proyecto web en Astro🚀


[Discord](https://discord.com/invite/chwAE86T6W)
[Desarrollador](https://linktr.ee/gatoartstudio)

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
.
├── astro.config.mjs
├── dist
│   ├── _astro
│   │   ├── hoisted.TOV5KKkp.js
│   │   ├── hoisted.Z0YVwTgx.js
│   │   └── index.CiM1GAXz.css
│   ├── CNAME
│   ├── downloads
│   │   └── index.html
│   ├── favicon.png
│   ├── index.html
│   ├── KLZ.gif
│   └── mods.html
├── LICENSE
├── package.json
├── package-lock.json
├── public
│   ├── CNAME
│   ├── favicon.png
│   ├── KLZ.gif
│   └── mods.html
├── README.md
├── src
│   ├── components
│   │   └── Card.astro
│   ├── env.d.ts
│   ├── js
│   │   └── main.js
│   ├── layouts
│   │   └── Layout.astro
│   └── pages
│       ├── downloads.astro
│       └── index.astro
└── tsconfig.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies (No es necesario)          |
| `npm update`              | REquerido para poder usar construir la web       |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat) of Astro.
