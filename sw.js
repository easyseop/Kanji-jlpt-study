/* 한자 공부 앱 서비스워커 — 오프라인 캐싱
   앱을 고치면 CACHE 버전을 올려라 (예: kanji-v2). */
const CACHE = "kanji-v11";
const ASSETS = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./icon-192.png",
  "./icon-512.png",
  "./icon-maskable-512.png",
  "./apple-touch-icon.png"
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // 필기순서 SVG(KanjiVG CDN): 캐시 우선, 없으면 받아서 캐시 → 한 번 본 글자는 오프라인에서도 표시
  if (url.hostname === "cdn.jsdelivr.net") {
    e.respondWith(
      caches.open(CACHE).then(async (c) => {
        const hit = await c.match(req);
        if (hit) return hit;
        try {
          const res = await fetch(req);
          if (res.ok) c.put(req, res.clone());
          return res;
        } catch (err) {
          return hit || Response.error();
        }
      })
    );
    return;
  }

  // 동일 출처: 캐시 우선, 네트워크 폴백(성공 시 캐시 갱신), 둘 다 실패하면 index.html
  if (url.origin === location.origin) {
    e.respondWith(
      caches.match(req).then((hit) =>
        hit ||
        fetch(req).then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
          return res;
        }).catch(() => caches.match("./index.html"))
      )
    );
  }
});
