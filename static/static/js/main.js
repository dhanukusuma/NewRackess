// =========================
// GLOBAL SIGNATUREPADS
// =========================
let sigInVisitor = null;
let sigInStaff = null;
let sigOutVisitor = null;
let sigOutStaff = null;

// =========================
// HELPER: RESET ALL PADS
// =========================
function resetSignaturePads() {
  sigInVisitor = null;
  sigInStaff = null;
  sigOutVisitor = null;
  sigOutStaff = null;
}

// =========================
// HELPER: RESIZE CANVAS (DPR-AWARE)
// =========================
function resizeCanvasWithDPR(canvas, sigPadInstance) {
  if (!canvas) return;

  const ratio = Math.max(window.devicePixelRatio || 1, 1);
  const rect = canvas.getBoundingClientRect();

  canvas.width = rect.width * ratio;
  canvas.height = rect.height * ratio;

  const ctx = canvas.getContext("2d");
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0); // scale ke DPR

  // tiap resize, clear biar gak korup
  if (sigPadInstance) {
    sigPadInstance.clear();
  }
}

// =========================
// INIT SEMUA SIGNATURE PAD
// =========================
function initSignaturePads() {
  // PINJAM - Pengunjung
  const canvasInVisitor = document.getElementById("canvas_in_visitor");
  if (canvasInVisitor) {
    resizeCanvasWithDPR(canvasInVisitor, sigInVisitor);
    sigInVisitor = new SignaturePad(canvasInVisitor, {
      backgroundColor: "#ffffff",
      penColor: "#000000",
    });
  } else {
    sigInVisitor = null;
  }

  // PINJAM - Petugas
  const canvasInStaff = document.getElementById("canvas_in_staff");
  if (canvasInStaff) {
    resizeCanvasWithDPR(canvasInStaff, sigInStaff);
    sigInStaff = new SignaturePad(canvasInStaff, {
      backgroundColor: "#ffffff",
      penColor: "#000000",
    });
  } else {
    sigInStaff = null;
  }

  // KEMBALI - Pengunjung
  const canvasOutVisitor = document.getElementById("canvas_out_visitor");
  if (canvasOutVisitor) {
    resizeCanvasWithDPR(canvasOutVisitor, sigOutVisitor);
    sigOutVisitor = new SignaturePad(canvasOutVisitor, {
      backgroundColor: "#ffffff",
      penColor: "#000000",
    });
  } else {
    sigOutVisitor = null;
  }

  // KEMBALI - Petugas
  const canvasOutStaff = document.getElementById("canvas_out_staff");
  if (canvasOutStaff) {
    resizeCanvasWithDPR(canvasOutStaff, sigOutStaff);
    sigOutStaff = new SignaturePad(canvasOutStaff, {
      backgroundColor: "#ffffff",
      penColor: "#000000",
    });
  } else {
    sigOutStaff = null;
  }
}

// =========================
// CLEAR SIGNATURE BY ID
// =========================
function clearSignature(canvasId) {
  switch (canvasId) {
    case "canvas_in_visitor":
      if (sigInVisitor) sigInVisitor.clear();
      break;
    case "canvas_in_staff":
      if (sigInStaff) sigInStaff.clear();
      break;
    case "canvas_out_visitor":
      if (sigOutVisitor) sigOutVisitor.clear();
      break;
    case "canvas_out_staff":
      if (sigOutStaff) sigOutStaff.clear();
      break;
  }
}

// =========================
// VALIDASI PINJAM
// =========================
function validateBorrowTTD() {
  const inputVisitor = document.getElementById("sig_in_visitor");
  const inputStaff = document.getElementById("sig_in_staff");

  if (!inputVisitor.value || !inputStaff.value) {
    alert("TTD pengunjung dan petugas (PINJAM) wajib diisi.");
    return false;
  }

  return true;
}

// =========================
// VALIDASI KEMBALI
// =========================
function validateReturnTTD() {
  const inputVisitor = document.getElementById("sig_out_visitor");
  const inputStaff = document.getElementById("sig_out_staff");

  if (sigOutVisitor && !sigOutVisitor.isEmpty()) {
    inputVisitor.value = sigOutVisitor.toDataURL("image/png");
  }

  if (sigOutStaff && !sigOutStaff.isEmpty()) {
    inputStaff.value = sigOutStaff.toDataURL("image/png");
  }

  if (!inputVisitor.value || !inputStaff.value) {
    alert("TTD pengunjung dan petugas (KEMBALI) wajib diisi.");
    return false;
  }

  return true;
}

// =========================
// GLOBAL: CLOSE MODAL + RESET
// =========================
function closeModal() {
  const modalContainer = document.getElementById("modal-container");
  if (modalContainer) {
    modalContainer.innerHTML = "";
  }
  resetSignaturePads();
}

// =========================
// BOOTSTRAP
// =========================
document.addEventListener("DOMContentLoaded", function () {
  // Init pertama kali (kalau ada canvas di halaman awal)
  initSignaturePads();

  // HTMX: setelah swap
  document.body.addEventListener("htmx:afterSwap", function (evt) {
    if (!evt.detail || !evt.detail.target) return;
    const target = evt.detail.target;

    // 1) Abis submit: row di tabel ke-update -> tutup modal + reset pad
    if (target.id === "key-table-body" || target.id === "laptop-table-body") {
      const modalContainer = document.getElementById("modal-container");
      if (modalContainer) {
        modalContainer.innerHTML = "";
      }
      resetSignaturePads();
    }

    // 2) Apapun yang baru di-swap bisa saja mengandung canvas
    //    (misal modal borrow/return baru) -> init ulang
    setTimeout(initSignaturePads, 0);
  });

  // Window resize / zoom -> resize ulang canvas + clear
  window.addEventListener("resize", function () {
    initSignaturePads();
  });

  // tombol Export Excel pakai filter yang aktif
  const btnExportExcel = document.getElementById("btn-export-excel");
  if (btnExportExcel) {
    btnExportExcel.addEventListener("click", function () {
      const form = document.getElementById("key-filter-form");
      if (!form) {
        window.open("/keys/export/excel", "_blank");
        return;
      }
      const formData = new FormData(form);
      const params = new URLSearchParams(formData).toString();
      const url = "/keys/export/excel" + (params ? "?" + params : "");
      window.open(url, "_blank");
    });
  }
});

// tombol Export PDF pakai filter aktif
const btnExportPdf = document.getElementById("btn-export-pdf");
if (btnExportPdf) {
  btnExportPdf.addEventListener("click", function () {
    const form = document.getElementById("key-filter-form");
    if (!form) {
      window.open("/keys/export/pdf", "_blank");
      return;
    }
    const formData = new FormData(form);
    const params = new URLSearchParams(formData).toString();
    const url = "/keys/export/pdf" + (params ? "?" + params : "");
    window.open(url, "_blank");
  });
}
