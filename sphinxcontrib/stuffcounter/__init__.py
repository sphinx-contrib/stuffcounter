# pylint: disable=line-too-long
"""
    sphinxcontrib.stuffcounter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A sphinx extension to count stuff.

    :copyright: Copyright 2018 by Louis Paternault <spalax@gresille.org>
    :license: Public domain, WTFPL, GNU GPLv2+, GNU AGPL, GNU LGPLv3+, 2-clause BSD, 3-clause BSD, Apache2, MIT, MPL, at your own choice. See https://framagit.org/spalax/sphinxcontrib-stuffcounter/blob/main/LICENSE.md for more information.
"""

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList

from sphinx.domains.std import StandardDomain
from sphinx.util.docutils import SphinxDirective

__version__ = "0.0.0"


class StuffNode(nodes.General, nodes.Element):
    """Stuff"""


class ContentNode(nodes.General, nodes.Element):
    """Content of stuff."""


def stuff_wrapper(directive, node, caption=None):
    """Parse caption, and append it to the node."""
    parsed = nodes.Element()
    if caption is None:
        caption_node = nodes.caption()
    else:
        directive.state.nested_parse(
            ViewList([caption], source=""), directive.content_offset, parsed
        )
        caption_node = nodes.caption(parsed[0].rawsource, "", *parsed[0].children)
        caption_node.source = parsed[0].source
        caption_node.line = parsed[0].line
    node += caption_node
    return node


class StuffDirective(SphinxDirective):
    """An environment for stuffs."""

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {"caption": directives.unchanged_required}

    def run(self):
        """Render this environment"""
        node = StuffNode("\n".join(self.content))

        caption = self.options.get("caption")
        if caption:
            node = stuff_wrapper(self, node, caption)
        else:
            node = stuff_wrapper(self, node)

        content = ContentNode()
        self.state.nested_parse(self.content, self.content_offset, content)
        node += content

        self.add_name(node)

        return [node]


class StuffDomain(StandardDomain):
    """Stuff domain"""

    name = "stuffcounter"
    label = "Stuff Counter"

    directives = {"stuff": StuffDirective}


################################################################################
# HTML
def html_visit_stuff_node(self, node):
    """Enter :class:`StuffNode` in HTML builder."""
    self.body.append(self.starttag(node, "div", CLASS="stuff"))


def html_depart_stuff_node(self, node):
    """Leave :class:`StuffNode` in HTML builder."""
    # pylint: disable=unused-argument
    self.body.append("</div>")


def html_visit_caption_node(self, node):
    """Enter :class:`CaptionNode` in HTML builder."""
    self.body.append(self.starttag(node, "div", CLASS="stuff-caption"))
    self.add_fignumber(node.parent)
    if node.astext():
        self.body.append(" — ")
        self.body.append(self.starttag(node, "span", CLASS="caption-text"))


def html_depart_caption_node(self, node):
    """Leave :class:`CaptionNode` in HTML builder."""
    # pylint: disable=unused-argument
    if node.astext():
        self.body.append("</span>")
    self.body.append("</div>")


def html_visit_content_node(self, node):
    """Enter :class:`ContentNode` in HTML builder."""
    self.body.append(self.starttag(node, "div", CLASS="stuff-content"))


def html_depart_content_node(self, node):
    """Leave :class:`ContentNode` in HTML builder."""
    # pylint: disable=unused-argument
    self.body.append("</div>")


################################################################################
# LaTeX


def latex_visit_stuff_node(self, node):
    """Enter :class:`StuffNode` in LaTeX builder."""
    # pylint: disable=unused-argument
    self.body.append(r"\begin{stuff}")


def latex_depart_stuff_node(self, node):
    """Leave :class:`StuffNode` in LaTeX builder."""
    self.body.append(self.hypertarget_to(node))
    self.body.append(r"\end{stuff}")
    self.body.append("\n")


def latex_visit_content_node(self, node):  # pylint: disable=unused-argument
    """Enter :class:`ContentNode` in LaTeX builder."""


def latex_depart_content_node(self, node):  # pylint: disable=unused-argument
    """Leave :class:`ContentNode` in LaTeX builder."""


def latex_visit_caption_node(self, node):
    """Enter :class:`CaptionNode` in LaTeX builder."""
    # pylint: disable=unused-argument
    if node.astext():
        self.body.append("[")


def latex_depart_caption_node(self, node):
    """Leave :class:`CaptionNode` in LaTeX builder."""
    # pylint: disable=unused-argument
    if node.astext():
        self.body.append("]")


################################################################################
# Setup


def generate_latex_preamble(app):
    """Hook called when builder has been inited."""
    config = app.builder.config
    if app.builder.name == "latex":
        if "preamble" not in config.latex_elements:
            config.latex_elements["preamble"] = ""
        config.latex_elements["preamble"] += r"\newtheorem{stuff}{Stuff}"


def init_numfig_format(app, config):
    """Initialize :confval:`numfig_format`."""
    # pylint: disable=unused-argument
    numfig_format = {"stuff": "Stuff %s"}

    # override default labels by configuration
    numfig_format.update(config.numfig_format)
    config.numfig_format = numfig_format


def setup(app):
    """Setup extension."""

    app.add_domain(StuffDomain)

    app.connect("builder-inited", generate_latex_preamble)
    app.connect("config-inited", init_numfig_format)

    app.add_css_file("stuff.css")

    app.add_enumerable_node(
        StuffNode,
        "stuff",
        html=(html_visit_stuff_node, html_depart_stuff_node),
        singlehtml=(html_visit_stuff_node, html_depart_stuff_node),
        latex=(latex_visit_stuff_node, latex_depart_stuff_node),
    )
    app.add_node(
        nodes.caption,
        override=True,
        html=(html_visit_caption_node, html_depart_caption_node),
        singlehtml=(html_visit_caption_node, html_depart_caption_node),
        latex=(latex_visit_caption_node, latex_depart_caption_node),
    )
    app.add_node(
        ContentNode,
        html=(html_visit_content_node, html_depart_content_node),
        singlehtml=(html_visit_content_node, html_depart_content_node),
        latex=(latex_visit_content_node, latex_depart_content_node),
    )

    return {"version": __version__, "parallel_read_safe": True}
