<div align="center">

<img src="https://raw.githubusercontent.com/WessYu/WessYu/main/readme-assets/WessYu-cover.svg" alt="WessYu — Software Developer" width="100%">

<br>

**Software Developer · React / TypeScript · Developer Tooling · Application Security**

I started in front-end and kept following the problems further down the stack. Today I build web products and the tooling around them — component governance, performance checks, security scans and CI gates.

[Portfolio](https://wessyu-arquivo.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/wesley-cruz2001/) · [Email](mailto:wess.c@proton.me)

</div>

---

## Engineering toolkit

<p align="center">
  <img src="https://raw.githubusercontent.com/WessYu/WessYu/main/readme-assets/engineering-toolkit.svg" alt="NEXUS, Component Vault, Velocity and SPECTER" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/WessYu/NEXUS"><strong>NEXUS</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/WessYu/component-vault"><strong>Component Vault</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/WessYu/velocity"><strong>Velocity</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/WessYu/SPECTER"><strong>SPECTER</strong></a>
</p>

### NEXUS

**One engineering gate for code quality, performance and application security.**

NEXUS orchestrates the three independent engines below through one CLI, normalizes their results and applies repository-level policy without hiding the evidence produced by each tool.

```text
Component Vault ── quality ──────┐
Velocity ───────── performance ──┼── NEXUS ── engineering gate
SPECTER ────────── security ─────┘
```

```bash
npm install -D @wess2001/nexus
npx nexus check .
```

[**Source ↗**](https://github.com/WessYu/NEXUS) · [**npm ↗**](https://www.npmjs.com/package/@wess2001/nexus)

---

### Component Vault

**AST-based component governance and design-system tooling for real codebases.**

- TypeScript Compiler API analysis across TS/TSX/JS/JSX
- repository-owned semantic and component policies
- brownfield baselines and PR enforcement
- deterministic autofix with guarded import resolution
- CLI, CI workflow and full-stack component workspace

[**Live product ↗**](https://component-vault-dun.vercel.app/) · [**Source ↗**](https://github.com/WessYu/component-vault) · [**npm ↗**](https://www.npmjs.com/package/@wess2001/component-vault)

---

### Velocity

**Performance diagnostics and regression control from source code to real runtime behavior.**

- parser-backed static analysis with lexical binding awareness
- build and emitted-asset measurement
- real Chromium lab metrics including FCP, LCP, CLS, TBT and TTFB
- benchmark and Node.js profiling workflows
- compatible baselines, CI regression gates, JSON and SARIF
- reviewable optimization plans with validation and rollback safeguards

[**Source ↗**](https://github.com/WessYu/velocity) · [**npm ↗**](https://www.npmjs.com/package/@wess2001/velocity)

---

### SPECTER

**Defensive application security from source to production.**

- source, secrets, dependencies and build-output analysis
- passive checks for deployed applications
- authorized, bounded active security testing
- stable findings, baselines and security regression gates
- JSON/SARIF reporting plus API and dashboard architecture
- explicit authorization, request budgets, rate limiting and non-destructive boundaries for active checks

[**Source ↗**](https://github.com/WessYu/SPECTER) · [**npm ↗**](https://www.npmjs.com/package/@wess2001/specter)

---

## Selected product work

| Project | What it demonstrates | Main stack |
| --- | --- | --- |
| [**Component Vault**](https://github.com/WessYu/component-vault) | Product UI, full-stack architecture, component governance and developer tooling | Next.js · React · TypeScript · Convex · Node.js |
| [**NEXUS**](https://github.com/WessYu/NEXUS) | Multi-engine orchestration, normalized reports, policy evaluation and release integration | Node.js · JavaScript · JSON Schema · CI |
| [**SPECTER**](https://github.com/WessYu/SPECTER) | Defensive AppSec, scanning architecture, API persistence and security gates | TypeScript · Fastify · PostgreSQL · Prisma · Next.js |
| [**Velocity**](https://github.com/WessYu/velocity) | Static analysis, browser measurement, benchmarking and regression control | Node.js · TypeScript · Babel AST · Chromium |
| [**Differenza**](https://github.com/WessYu/differenza-redesign) | UI/UX audit, visual redesign, responsive implementation and content hierarchy | Front-End · Responsive UI · UI/UX |

[**Explore all repositories →**](https://github.com/WessYu?tab=repositories)

---

## Core stack

<p align="center">
  <img src="https://img.shields.io/badge/React-111111?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Next.js-111111?style=for-the-badge&logo=nextdotjs&logoColor=FFFFFF" alt="Next.js" />
  <img src="https://img.shields.io/badge/TypeScript-111111?style=for-the-badge&logo=typescript&logoColor=3178C6" alt="TypeScript" />
  <img src="https://img.shields.io/badge/JavaScript-111111?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Tailwind-111111?style=for-the-badge&logo=tailwindcss&logoColor=38BDF8" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/Node.js-111111?style=for-the-badge&logo=nodedotjs&logoColor=5FA04E" alt="Node.js" />
  <img src="https://img.shields.io/badge/Fastify-111111?style=for-the-badge&logo=fastify&logoColor=FFFFFF" alt="Fastify" />
  <img src="https://img.shields.io/badge/PostgreSQL-111111?style=for-the-badge&logo=postgresql&logoColor=4169E1" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Prisma-111111?style=for-the-badge&logo=prisma&logoColor=FFFFFF" alt="Prisma" />
  <img src="https://img.shields.io/badge/Playwright-111111?style=for-the-badge&logo=playwright&logoColor=2EAD33" alt="Playwright" />
  <img src="https://img.shields.io/badge/GitHub_Actions-111111?style=for-the-badge&logo=githubactions&logoColor=2088FF" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Figma-111111?style=for-the-badge&logo=figma&logoColor=F24E1E" alt="Figma" />
</p>

---

## How I build

My base is still front-end engineering: interface quality, component APIs, accessibility, responsive behavior and product polish.

The difference is that I now follow those problems further down the stack. If maintainability needs static analysis, I build the analyzer. If performance needs evidence, I measure the build and browser. If security needs a repeatable gate, I turn the checks into tooling and CI policy.

That progression is what connects my current work: **product engineering on the surface, engineering systems underneath it.**

---

## Open to opportunities

I'm looking for a **Junior Software Developer / Front-End / Full-Stack** role where I can contribute with React, TypeScript and Node.js while continuing to grow across backend systems, developer tooling and application security.

Remote opportunities are especially welcome.

---

<div align="center">

[Portfolio](https://wessyu-arquivo.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/wesley-cruz2001/) · [Email](mailto:wess.c@proton.me)

</div>
