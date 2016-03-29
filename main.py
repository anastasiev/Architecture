from model import *
from view import *
from controller import *
import pydoc
import sys
import coverage

pydoc.help(sys)

controller = MatchesController()
controller.navigation()

