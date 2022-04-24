import argparse

# See https://docs.python.org/3/library/argparse.html
main_parser = argparse.ArgumentParser(description="A WIP dotfile manager")
subparsers = main_parser.add_subparsers(
    title="subcommands",
)
main_parser.add_argument(
    "-i",
    "--interactive",
    help="run in interactive mode",
    action="store_true"
)


parser_add = subparsers.add_parser("add", help="Start tracking a dotfile")
parser_add.add_argument(
    "name",
    help="The (arbitrary) name for this dotfile",
    type=str
)
parser_add.add_argument(
    "link-location",
    help="The location for this dotfile to be linked to (where other programs will look for it)",
    type=str
)
parser_add.add_argument(
    "real-location",
    help="The real location of the file",
    type=str

)
parser_add.add_argument(
    "-m",
    "--move",
    help="whether to move the file to the reccomended location",
    action="store_true"
)


parser_remove = subparsers.add_parser("remove", help="Stop tracking a dotfile")
parser_remove.add_argument(
    "name",
    help="The name of the dotfile, set upon creation",
    type=str
)
parser_remove.add_argument(
    "-d",
    "--delete",
    help="also delete the symlink",
    action="store_true"
)
parser_remove.add_argument(
    "-m",
    "--move",
    help="move file to symlinked location",
    action="store_true"
)


parser_tag = subparsers.add_parser("tag", help="Manage dotfile tags")
tag_subparsers = parser_tag.add_subparsers(title="subcommands")
parser_tag_create = tag_subparsers.add_parser("create", help="create tag")
parser_tag_create.add_argument(
    "name",
    type=str,
    help="the tag name"
)
# TODO: allow adding arbitrary dotfiles by name with any other args
parser_tag_remove = tag_subparsers.add_parser("delete", help="delete tag")
parser_tag_remove.add_argument(
    "name",
    help="the name of the tag to delete",
    type=str
)

parser_tag_add = tag_subparsers.add_parser("add", help="add a tag to dotfile(s)")
parser_tag_add.add_argument(
    "tag",
    type=str,
    help="The tag to add to the dotfiles"
)
parser_tag_add.add_argument(
    "dotfiles",
    nargs="*",
    type=str,
    help="The dotfiles to add the tag to"
)


args = main_parser.parse_args()

