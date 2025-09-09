Propuesta en 3 etapas. Enfoque monorepo, multitenant, Mobile + User Portal + Admin Portal. Operativa con tus comandos.

# Etapa 1 — Método de especificación iterativa con ChatGPT

Objetivo: convertir ideas sueltas en especificaciones versionadas y ejecutables.

**Estructura base (monorepo)**

* `/apps/mobile`, `/apps/user-portal`, `/apps/admin-portal`
* `/services/<microservicio>`
* `/docs` → `documento-rector.md`, `mermaid/`, `ADR/`, `Consolidados/`, `categorias/*`
* Raíz: `ROADMAP.md`, `ROADMAP_user.md`, `ROADMAP_admin.md`, `ROADMAP_mobile.md`, `CHANGELOG.md`, `00-INDEX.md`, `out/latest.patch`

**Plantillas mínimas**

* `plans/<dominio>/<microservicio>.md`

  * Propósito, límites, APIs, eventos, datos, dependencias, riesgos, SLO, costos.
* `docs/ADR/ADR-YYYYMMDD-<decision>.md`

  * Contexto, Decisión, Consecuencias, Alternativas.
* `docs/mermaid/<diagrama>.md`

  * Diagramas C4 + secuencia por flujo crítico.

**Ciclo de trabajo con ChatGPT**

1. Tú describes intención en una frase.
2. Comando: `plan de <dominio>/<servicio>` → genero plan y endpoints iniciales.
3. Comando: `endpoints para <dominio>/<función>` → genero OpenAPI + flujos.
4. Comando: `prioridades …` → ordeno backlog, afecto ROADMAP\*.
5. Comando: `actualiza repo` → produzco parches `out/latest.patch` + dif de archivos.
6. Validación: yo marco `TODO:` explícitos. Sin confirmaciones ambiguas.

**Reglas de calidad obligatorias**

* Un servicio = una responsabilidad.
* Seguridad por defecto: OAuth2/OIDC, tenants aislados por `tenant_id` en claims, ABAC por ámbito.
* Observabilidad: traces, logs estructurados, métricas por tenant.
* Testing: contrato (Pact), E2E por dominio, datos sintéticos multi-tenant.
* CI/CD: envs por rama, migraciones idempotentes, rollback.
* Costos: budgets por servicio y alertas.

# Etapa 2 — Ingesta y consolidación de +150 documentos de Drive

Objetivo: eliminar “archivos sueltos” y crear una sola biblioteca coherente.

**Proceso**

1. Comando: `releer drive` → indexo todo y genero `00-INDEX.md` mapeando **Fuente → Categoría**:
   01-Visión, 02-Gobernanza, 03-Arquitectura, 04-Datos, 05-Módulos, 06-Legal-Compliance, 07-UI-UX, 08-DevOps, 09-Requisitos, 10-Backlog, 11-Investigaciones, 12-Glosario, 13-ADR, 99-Misceláneo.
2. Por categoría creo `Consolidados/<NN-Nombre>-Consolidado.md` con secciones `=== Fuente: <archivo> ===` y extracción de **áreas críticas**.
3. Identifico duplicados y obsoletos. Marco `PROPUESTO_ELIMINAR` con razón y referencia del reemplazo.
4. Actualizo `docs/documento-rector.md` con: visión global, áreas críticas, dominios, arquitectura, catálogo de funciones y endpoints, planes por microservicio, roadmaps, ADRs, apéndices.
5. Genero `CHANGELOG.md` con cada pasada.

**Criterios de movimiento/eliminación**

* Un documento se conserva solo si aporta algo no contenido en su consolidado.
* Toda decisión técnica debe tener ADR asociado.
* Todo requerimiento funcional migra a `09-Requisitos` y a `10-Backlog` si es tarea.

# Etapa 3 — Acceso desde cualquier dispositivo y evolución continua

Objetivo: operar la biblioteca única y seguir definiendo alcance sin desorden.

**Operativa**

* Fuente de verdad: el monorepo. Drive queda solo como entrada de una sola dirección hasta vaciarlo.
* Comando maestro: `#procesar`

  * Lee ideas nuevas en `10-Backlog` y notas en `99-Misceláneo`.
  * Consolida en categorías.
  * Depura especificaciones superadas.
  * Revalida impactos entre servicios y actualiza ADRs, ROADMAP\*, `documento-rector.md`, `00-INDEX.md`, Consolidados.
  * Emite `out/latest.patch` y `CHANGELOG.md`.
* Acceso: GitHub como biblioteca única. Lectura vía web UI o Git client en cualquier dispositivo.

**Flujo de cambios**

1. Propones cambio → `prioridades …` o `plan de …`
2. Yo genero dif y TODOs → tú validas.
3. `#procesar` → sincronizo todo y cierro obsoletos.

---

## Artefactos que mantendré siempre

* `docs/documento-rector.md`
* `docs/mermaid/*`
* `plans/<dominio>/<microservicio>.md`
* `ROADMAP*.md`
* `CHANGELOG.md`
* `00-INDEX.md` + `Consolidados/*`
* `out/latest.patch`

## Áreas críticas a vigilar desde el día 1

* Aislamiento multitenant: claves de partición, límites por tenant, exportaciones filtradas.
* Identidad y roles por dominio: Mobile/User/Admin con flujos distintos.
* Modelo de datos canónico y migraciones.
* Catálogo de eventos y contratos entre servicios.
* Costeo y SLO por servicio.
* Privacidad y cumplimiento local.

## Próximos pasos

1. `generar documento rector` → creo la primera versión con esqueleto completo.
2. `releer drive` → indexo y creo consolidados.
3. `prioridades <global|user|admin|mobile>` → construyo ROADMAPs.
4. Cuando quieras sincronizar todo: `#procesar`.
