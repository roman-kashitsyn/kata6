#let slugs = sys.inputs.slugs.split(",")
#let card-font = sys.inputs.at("font", default: "DejaVu Sans Mono")

#set document(title: "kata6 algorithm cards")
#set page(paper: "a6", flipped: true, margin: (x: 8mm, y: 6mm))
#set text(size: 9pt)
#show raw: set text(font: card-font)

#for (i, slug) in slugs.enumerate() {
  if i > 0 { pagebreak() }
  block(
    height: 100%,
    width: 100%,
    align(
      horizon + left,
      raw(read("src/" + slug + ".py"), lang: "python", block: true),
    ),
  )
}
