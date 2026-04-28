# Generated from SonicRPG.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,230,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,1,2,1,2,1,
        2,3,2,85,8,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,3,4,94,8,4,1,4,1,4,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,5,10,120,8,10,10,10,12,10,123,9,10,1,10,
        1,10,1,10,1,10,5,10,129,8,10,10,10,12,10,132,9,10,1,10,3,10,135,
        8,10,1,10,1,10,1,10,1,11,1,11,3,11,142,8,11,1,11,1,11,5,11,146,8,
        11,10,11,12,11,149,9,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,
        1,13,3,13,160,8,13,1,13,1,13,1,14,1,14,3,14,166,8,14,1,14,1,14,1,
        15,1,15,1,15,1,16,1,16,3,16,175,8,16,1,16,1,16,1,17,1,17,1,17,1,
        18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,1,22,3,22,199,8,22,1,23,1,23,1,24,1,24,1,24,1,24,1,
        24,1,24,3,24,209,8,24,1,24,1,24,1,24,1,24,1,24,1,24,5,24,217,8,24,
        10,24,12,24,220,9,24,1,25,1,25,1,25,1,25,3,25,226,8,25,1,26,1,26,
        1,26,0,1,48,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,0,7,1,0,27,34,3,0,9,9,35,36,58,58,3,0,
        9,9,37,38,58,58,1,0,39,44,1,0,47,48,1,0,45,46,2,0,1,5,36,37,236,
        0,57,1,0,0,0,2,79,1,0,0,0,4,81,1,0,0,0,6,88,1,0,0,0,8,90,1,0,0,0,
        10,97,1,0,0,0,12,99,1,0,0,0,14,103,1,0,0,0,16,105,1,0,0,0,18,109,
        1,0,0,0,20,113,1,0,0,0,22,139,1,0,0,0,24,154,1,0,0,0,26,157,1,0,
        0,0,28,163,1,0,0,0,30,169,1,0,0,0,32,172,1,0,0,0,34,178,1,0,0,0,
        36,181,1,0,0,0,38,184,1,0,0,0,40,187,1,0,0,0,42,190,1,0,0,0,44,198,
        1,0,0,0,46,200,1,0,0,0,48,208,1,0,0,0,50,225,1,0,0,0,52,227,1,0,
        0,0,54,56,3,2,1,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,
        1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,
        80,3,4,2,0,63,80,3,8,4,0,64,80,3,12,6,0,65,80,3,16,8,0,66,80,3,18,
        9,0,67,80,3,20,10,0,68,80,3,22,11,0,69,80,3,24,12,0,70,80,3,26,13,
        0,71,80,3,28,14,0,72,80,3,30,15,0,73,80,3,32,16,0,74,80,3,34,17,
        0,75,80,3,36,18,0,76,80,3,38,19,0,77,80,3,40,20,0,78,80,3,42,21,
        0,79,62,1,0,0,0,79,63,1,0,0,0,79,64,1,0,0,0,79,65,1,0,0,0,79,66,
        1,0,0,0,79,67,1,0,0,0,79,68,1,0,0,0,79,69,1,0,0,0,79,70,1,0,0,0,
        79,71,1,0,0,0,79,72,1,0,0,0,79,73,1,0,0,0,79,74,1,0,0,0,79,75,1,
        0,0,0,79,76,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,3,1,0,0,0,81,
        82,5,6,0,0,82,84,3,6,3,0,83,85,5,56,0,0,84,83,1,0,0,0,84,85,1,0,
        0,0,85,86,1,0,0,0,86,87,5,53,0,0,87,5,1,0,0,0,88,89,7,0,0,0,89,7,
        1,0,0,0,90,91,5,7,0,0,91,93,3,10,5,0,92,94,5,56,0,0,93,92,1,0,0,
        0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,53,0,0,96,9,1,0,0,0,97,98,
        7,1,0,0,98,11,1,0,0,0,99,100,5,8,0,0,100,101,3,14,7,0,101,102,5,
        53,0,0,102,13,1,0,0,0,103,104,7,2,0,0,104,15,1,0,0,0,105,106,5,10,
        0,0,106,107,5,11,0,0,107,108,5,53,0,0,108,17,1,0,0,0,109,110,5,12,
        0,0,110,111,5,57,0,0,111,112,5,53,0,0,112,19,1,0,0,0,113,114,5,13,
        0,0,114,115,5,49,0,0,115,116,3,44,22,0,116,117,5,50,0,0,117,121,
        5,51,0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,134,
        5,52,0,0,125,126,5,14,0,0,126,130,5,51,0,0,127,129,3,2,1,0,128,127,
        1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,
        1,0,0,0,132,130,1,0,0,0,133,135,5,52,0,0,134,125,1,0,0,0,134,135,
        1,0,0,0,135,136,1,0,0,0,136,137,5,15,0,0,137,138,5,53,0,0,138,21,
        1,0,0,0,139,141,5,16,0,0,140,142,5,56,0,0,141,140,1,0,0,0,141,142,
        1,0,0,0,142,143,1,0,0,0,143,147,5,51,0,0,144,146,3,2,1,0,145,144,
        1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,150,
        1,0,0,0,149,147,1,0,0,0,150,151,5,52,0,0,151,152,5,17,0,0,152,153,
        5,53,0,0,153,23,1,0,0,0,154,155,5,18,0,0,155,156,5,53,0,0,156,25,
        1,0,0,0,157,159,5,19,0,0,158,160,5,57,0,0,159,158,1,0,0,0,159,160,
        1,0,0,0,160,161,1,0,0,0,161,162,5,53,0,0,162,27,1,0,0,0,163,165,
        5,20,0,0,164,166,5,57,0,0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,
        1,0,0,0,167,168,5,53,0,0,168,29,1,0,0,0,169,170,5,21,0,0,170,171,
        5,53,0,0,171,31,1,0,0,0,172,174,5,22,0,0,173,175,5,56,0,0,174,173,
        1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,5,53,0,0,177,33,
        1,0,0,0,178,179,5,23,0,0,179,180,5,53,0,0,180,35,1,0,0,0,181,182,
        5,24,0,0,182,183,5,53,0,0,183,37,1,0,0,0,184,185,5,26,0,0,185,186,
        5,53,0,0,186,39,1,0,0,0,187,188,5,25,0,0,188,189,5,53,0,0,189,41,
        1,0,0,0,190,191,3,48,24,0,191,192,5,53,0,0,192,43,1,0,0,0,193,194,
        3,48,24,0,194,195,3,46,23,0,195,196,3,48,24,0,196,199,1,0,0,0,197,
        199,3,48,24,0,198,193,1,0,0,0,198,197,1,0,0,0,199,45,1,0,0,0,200,
        201,7,3,0,0,201,47,1,0,0,0,202,203,6,24,-1,0,203,204,5,49,0,0,204,
        205,3,48,24,0,205,206,5,50,0,0,206,209,1,0,0,0,207,209,3,50,25,0,
        208,202,1,0,0,0,208,207,1,0,0,0,209,218,1,0,0,0,210,211,10,4,0,0,
        211,212,7,4,0,0,212,217,3,48,24,5,213,214,10,3,0,0,214,215,7,5,0,
        0,215,217,3,48,24,4,216,210,1,0,0,0,216,213,1,0,0,0,217,220,1,0,
        0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,49,1,0,0,0,220,218,1,0,0,
        0,221,226,5,56,0,0,222,226,5,57,0,0,223,226,5,58,0,0,224,226,3,52,
        26,0,225,221,1,0,0,0,225,222,1,0,0,0,225,223,1,0,0,0,225,224,1,0,
        0,0,226,51,1,0,0,0,227,228,7,6,0,0,228,53,1,0,0,0,17,57,79,84,93,
        121,130,134,141,147,159,165,174,198,208,216,218,225
    ]

class SonicRPGParser ( Parser ):

    grammarFileName = "SonicRPG.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'position'", "'x'", "'y'", "'boss_unlocked'", 
                     "'game_over'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'>'", "'<'", "'>='", "'<='", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "MOVE", "COLLECT", "USE", 
                      "TOKEN", "FIGHT", "BOSS", "SAY", "IF", "ELSE", "ENDIF", 
                      "LOOP", "ENDLOOP", "EXIT", "SAVE", "LOAD", "INVENTORY", 
                      "WAIT", "LOOK", "STATUS", "MAP", "HELP", "UP", "DOWN", 
                      "LEFT", "RIGHT", "NORTH", "SOUTH", "EAST", "WEST", 
                      "RING", "RINGS", "SPEED", "CHECKPOINT", "GT", "LT", 
                      "GTE", "LTE", "EQ", "NEQ", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "SEMICOLON", "COMMA", "DOT", "NUMBER", "STRING", "IDENTIFIER", 
                      "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_moveStatement = 2
    RULE_direction = 3
    RULE_collectStatement = 4
    RULE_collectTarget = 5
    RULE_useStatement = 6
    RULE_useTarget = 7
    RULE_fightStatement = 8
    RULE_sayStatement = 9
    RULE_ifStatement = 10
    RULE_loopStatement = 11
    RULE_exitStatement = 12
    RULE_saveStatement = 13
    RULE_loadStatement = 14
    RULE_inventoryStatement = 15
    RULE_waitStatement = 16
    RULE_lookStatement = 17
    RULE_statusStatement = 18
    RULE_helpStatement = 19
    RULE_mapStatement = 20
    RULE_expressionStatement = 21
    RULE_condition = 22
    RULE_compareOp = 23
    RULE_expression = 24
    RULE_atom = 25
    RULE_gameProperty = 26

    ruleNames =  [ "program", "statement", "moveStatement", "direction", 
                   "collectStatement", "collectTarget", "useStatement", 
                   "useTarget", "fightStatement", "sayStatement", "ifStatement", 
                   "loopStatement", "exitStatement", "saveStatement", "loadStatement", 
                   "inventoryStatement", "waitStatement", "lookStatement", 
                   "statusStatement", "helpStatement", "mapStatement", "expressionStatement", 
                   "condition", "compareOp", "expression", "atom", "gameProperty" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    MOVE=6
    COLLECT=7
    USE=8
    TOKEN=9
    FIGHT=10
    BOSS=11
    SAY=12
    IF=13
    ELSE=14
    ENDIF=15
    LOOP=16
    ENDLOOP=17
    EXIT=18
    SAVE=19
    LOAD=20
    INVENTORY=21
    WAIT=22
    LOOK=23
    STATUS=24
    MAP=25
    HELP=26
    UP=27
    DOWN=28
    LEFT=29
    RIGHT=30
    NORTH=31
    SOUTH=32
    EAST=33
    WEST=34
    RING=35
    RINGS=36
    SPEED=37
    CHECKPOINT=38
    GT=39
    LT=40
    GTE=41
    LTE=42
    EQ=43
    NEQ=44
    PLUS=45
    MINUS=46
    MULTIPLY=47
    DIVIDE=48
    LPAREN=49
    RPAREN=50
    LBRACE=51
    RBRACE=52
    SEMICOLON=53
    COMMA=54
    DOT=55
    NUMBER=56
    STRING=57
    IDENTIFIER=58
    WS=59
    COMMENT=60
    BLOCK_COMMENT=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SonicRPGParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SonicRPGParser.StatementContext)
            else:
                return self.getTypedRuleContext(SonicRPGParser.StatementContext,i)


        def getRuleIndex(self):
            return SonicRPGParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SonicRPGParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 504966314511382014) != 0):
                self.state = 54
                self.statement()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(SonicRPGParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.MoveStatementContext,0)


        def collectStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.CollectStatementContext,0)


        def useStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.UseStatementContext,0)


        def fightStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.FightStatementContext,0)


        def sayStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.SayStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.LoopStatementContext,0)


        def exitStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.ExitStatementContext,0)


        def saveStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.SaveStatementContext,0)


        def loadStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.LoadStatementContext,0)


        def inventoryStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.InventoryStatementContext,0)


        def waitStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.WaitStatementContext,0)


        def lookStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.LookStatementContext,0)


        def statusStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.StatusStatementContext,0)


        def helpStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.HelpStatementContext,0)


        def mapStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.MapStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(SonicRPGParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return SonicRPGParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SonicRPGParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.moveStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.collectStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.useStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.fightStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.sayStatement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.ifStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.loopStatement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.exitStatement()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 9)
                self.state = 70
                self.saveStatement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 10)
                self.state = 71
                self.loadStatement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 11)
                self.state = 72
                self.inventoryStatement()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 12)
                self.state = 73
                self.waitStatement()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 13)
                self.state = 74
                self.lookStatement()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 14)
                self.state = 75
                self.statusStatement()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 15)
                self.state = 76
                self.helpStatement()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 16)
                self.state = 77
                self.mapStatement()
                pass
            elif token in [1, 2, 3, 4, 5, 36, 37, 49, 56, 57, 58]:
                self.enterOuterAlt(localctx, 17)
                self.state = 78
                self.expressionStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVE(self):
            return self.getToken(SonicRPGParser.MOVE, 0)

        def direction(self):
            return self.getTypedRuleContext(SonicRPGParser.DirectionContext,0)


        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def NUMBER(self):
            return self.getToken(SonicRPGParser.NUMBER, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_moveStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveStatement" ):
                listener.enterMoveStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveStatement" ):
                listener.exitMoveStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveStatement" ):
                return visitor.visitMoveStatement(self)
            else:
                return visitor.visitChildren(self)




    def moveStatement(self):

        localctx = SonicRPGParser.MoveStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_moveStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SonicRPGParser.MOVE)
            self.state = 82
            self.direction()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 83
                self.match(SonicRPGParser.NUMBER)


            self.state = 86
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UP(self):
            return self.getToken(SonicRPGParser.UP, 0)

        def DOWN(self):
            return self.getToken(SonicRPGParser.DOWN, 0)

        def LEFT(self):
            return self.getToken(SonicRPGParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(SonicRPGParser.RIGHT, 0)

        def NORTH(self):
            return self.getToken(SonicRPGParser.NORTH, 0)

        def SOUTH(self):
            return self.getToken(SonicRPGParser.SOUTH, 0)

        def EAST(self):
            return self.getToken(SonicRPGParser.EAST, 0)

        def WEST(self):
            return self.getToken(SonicRPGParser.WEST, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirection" ):
                listener.enterDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirection" ):
                listener.exitDirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirection" ):
                return visitor.visitDirection(self)
            else:
                return visitor.visitChildren(self)




    def direction(self):

        localctx = SonicRPGParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_direction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34225520640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLLECT(self):
            return self.getToken(SonicRPGParser.COLLECT, 0)

        def collectTarget(self):
            return self.getTypedRuleContext(SonicRPGParser.CollectTargetContext,0)


        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def NUMBER(self):
            return self.getToken(SonicRPGParser.NUMBER, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_collectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectStatement" ):
                listener.enterCollectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectStatement" ):
                listener.exitCollectStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectStatement" ):
                return visitor.visitCollectStatement(self)
            else:
                return visitor.visitChildren(self)




    def collectStatement(self):

        localctx = SonicRPGParser.CollectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_collectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SonicRPGParser.COLLECT)
            self.state = 91
            self.collectTarget()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 92
                self.match(SonicRPGParser.NUMBER)


            self.state = 95
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CollectTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RING(self):
            return self.getToken(SonicRPGParser.RING, 0)

        def RINGS(self):
            return self.getToken(SonicRPGParser.RINGS, 0)

        def TOKEN(self):
            return self.getToken(SonicRPGParser.TOKEN, 0)

        def IDENTIFIER(self):
            return self.getToken(SonicRPGParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_collectTarget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollectTarget" ):
                listener.enterCollectTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollectTarget" ):
                listener.exitCollectTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCollectTarget" ):
                return visitor.visitCollectTarget(self)
            else:
                return visitor.visitChildren(self)




    def collectTarget(self):

        localctx = SonicRPGParser.CollectTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_collectTarget)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 288230479230927360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(SonicRPGParser.USE, 0)

        def useTarget(self):
            return self.getTypedRuleContext(SonicRPGParser.UseTargetContext,0)


        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_useStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseStatement" ):
                listener.enterUseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseStatement" ):
                listener.exitUseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseStatement" ):
                return visitor.visitUseStatement(self)
            else:
                return visitor.visitChildren(self)




    def useStatement(self):

        localctx = SonicRPGParser.UseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_useStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(SonicRPGParser.USE)
            self.state = 100
            self.useTarget()
            self.state = 101
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN(self):
            return self.getToken(SonicRPGParser.TOKEN, 0)

        def SPEED(self):
            return self.getToken(SonicRPGParser.SPEED, 0)

        def CHECKPOINT(self):
            return self.getToken(SonicRPGParser.CHECKPOINT, 0)

        def IDENTIFIER(self):
            return self.getToken(SonicRPGParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_useTarget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseTarget" ):
                listener.enterUseTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseTarget" ):
                listener.exitUseTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseTarget" ):
                return visitor.visitUseTarget(self)
            else:
                return visitor.visitChildren(self)




    def useTarget(self):

        localctx = SonicRPGParser.UseTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_useTarget)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 288230788468572672) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FightStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIGHT(self):
            return self.getToken(SonicRPGParser.FIGHT, 0)

        def BOSS(self):
            return self.getToken(SonicRPGParser.BOSS, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_fightStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFightStatement" ):
                listener.enterFightStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFightStatement" ):
                listener.exitFightStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFightStatement" ):
                return visitor.visitFightStatement(self)
            else:
                return visitor.visitChildren(self)




    def fightStatement(self):

        localctx = SonicRPGParser.FightStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fightStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(SonicRPGParser.FIGHT)
            self.state = 106
            self.match(SonicRPGParser.BOSS)
            self.state = 107
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SayStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SAY(self):
            return self.getToken(SonicRPGParser.SAY, 0)

        def STRING(self):
            return self.getToken(SonicRPGParser.STRING, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_sayStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSayStatement" ):
                listener.enterSayStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSayStatement" ):
                listener.exitSayStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSayStatement" ):
                return visitor.visitSayStatement(self)
            else:
                return visitor.visitChildren(self)




    def sayStatement(self):

        localctx = SonicRPGParser.SayStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sayStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(SonicRPGParser.SAY)
            self.state = 110
            self.match(SonicRPGParser.STRING)
            self.state = 111
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SonicRPGParser.IF, 0)

        def LPAREN(self):
            return self.getToken(SonicRPGParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(SonicRPGParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(SonicRPGParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SonicRPGParser.LBRACE)
            else:
                return self.getToken(SonicRPGParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SonicRPGParser.RBRACE)
            else:
                return self.getToken(SonicRPGParser.RBRACE, i)

        def ENDIF(self):
            return self.getToken(SonicRPGParser.ENDIF, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SonicRPGParser.StatementContext)
            else:
                return self.getTypedRuleContext(SonicRPGParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(SonicRPGParser.ELSE, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SonicRPGParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(SonicRPGParser.IF)
            self.state = 114
            self.match(SonicRPGParser.LPAREN)
            self.state = 115
            self.condition()
            self.state = 116
            self.match(SonicRPGParser.RPAREN)
            self.state = 117
            self.match(SonicRPGParser.LBRACE)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 504966314511382014) != 0):
                self.state = 118
                self.statement()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(SonicRPGParser.RBRACE)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 125
                self.match(SonicRPGParser.ELSE)
                self.state = 126
                self.match(SonicRPGParser.LBRACE)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 504966314511382014) != 0):
                    self.state = 127
                    self.statement()
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 133
                self.match(SonicRPGParser.RBRACE)


            self.state = 136
            self.match(SonicRPGParser.ENDIF)
            self.state = 137
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(SonicRPGParser.LOOP, 0)

        def LBRACE(self):
            return self.getToken(SonicRPGParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SonicRPGParser.RBRACE, 0)

        def ENDLOOP(self):
            return self.getToken(SonicRPGParser.ENDLOOP, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def NUMBER(self):
            return self.getToken(SonicRPGParser.NUMBER, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SonicRPGParser.StatementContext)
            else:
                return self.getTypedRuleContext(SonicRPGParser.StatementContext,i)


        def getRuleIndex(self):
            return SonicRPGParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = SonicRPGParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(SonicRPGParser.LOOP)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 140
                self.match(SonicRPGParser.NUMBER)


            self.state = 143
            self.match(SonicRPGParser.LBRACE)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 504966314511382014) != 0):
                self.state = 144
                self.statement()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(SonicRPGParser.RBRACE)
            self.state = 151
            self.match(SonicRPGParser.ENDLOOP)
            self.state = 152
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT(self):
            return self.getToken(SonicRPGParser.EXIT, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_exitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExitStatement" ):
                listener.enterExitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExitStatement" ):
                listener.exitExitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExitStatement" ):
                return visitor.visitExitStatement(self)
            else:
                return visitor.visitChildren(self)




    def exitStatement(self):

        localctx = SonicRPGParser.ExitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(SonicRPGParser.EXIT)
            self.state = 155
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaveStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SAVE(self):
            return self.getToken(SonicRPGParser.SAVE, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def STRING(self):
            return self.getToken(SonicRPGParser.STRING, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_saveStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaveStatement" ):
                listener.enterSaveStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaveStatement" ):
                listener.exitSaveStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaveStatement" ):
                return visitor.visitSaveStatement(self)
            else:
                return visitor.visitChildren(self)




    def saveStatement(self):

        localctx = SonicRPGParser.SaveStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_saveStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(SonicRPGParser.SAVE)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 158
                self.match(SonicRPGParser.STRING)


            self.state = 161
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(SonicRPGParser.LOAD, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def STRING(self):
            return self.getToken(SonicRPGParser.STRING, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_loadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStatement" ):
                listener.enterLoadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStatement" ):
                listener.exitLoadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStatement" ):
                return visitor.visitLoadStatement(self)
            else:
                return visitor.visitChildren(self)




    def loadStatement(self):

        localctx = SonicRPGParser.LoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loadStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(SonicRPGParser.LOAD)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 164
                self.match(SonicRPGParser.STRING)


            self.state = 167
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InventoryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INVENTORY(self):
            return self.getToken(SonicRPGParser.INVENTORY, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_inventoryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInventoryStatement" ):
                listener.enterInventoryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInventoryStatement" ):
                listener.exitInventoryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInventoryStatement" ):
                return visitor.visitInventoryStatement(self)
            else:
                return visitor.visitChildren(self)




    def inventoryStatement(self):

        localctx = SonicRPGParser.InventoryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_inventoryStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(SonicRPGParser.INVENTORY)
            self.state = 170
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT(self):
            return self.getToken(SonicRPGParser.WAIT, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def NUMBER(self):
            return self.getToken(SonicRPGParser.NUMBER, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_waitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitStatement" ):
                listener.enterWaitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitStatement" ):
                listener.exitWaitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitStatement" ):
                return visitor.visitWaitStatement(self)
            else:
                return visitor.visitChildren(self)




    def waitStatement(self):

        localctx = SonicRPGParser.WaitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_waitStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(SonicRPGParser.WAIT)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 173
                self.match(SonicRPGParser.NUMBER)


            self.state = 176
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LookStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOK(self):
            return self.getToken(SonicRPGParser.LOOK, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_lookStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLookStatement" ):
                listener.enterLookStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLookStatement" ):
                listener.exitLookStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLookStatement" ):
                return visitor.visitLookStatement(self)
            else:
                return visitor.visitChildren(self)




    def lookStatement(self):

        localctx = SonicRPGParser.LookStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lookStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(SonicRPGParser.LOOK)
            self.state = 179
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatusStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATUS(self):
            return self.getToken(SonicRPGParser.STATUS, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_statusStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatusStatement" ):
                listener.enterStatusStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatusStatement" ):
                listener.exitStatusStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatusStatement" ):
                return visitor.visitStatusStatement(self)
            else:
                return visitor.visitChildren(self)




    def statusStatement(self):

        localctx = SonicRPGParser.StatusStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statusStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(SonicRPGParser.STATUS)
            self.state = 182
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HelpStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HELP(self):
            return self.getToken(SonicRPGParser.HELP, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_helpStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelpStatement" ):
                listener.enterHelpStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelpStatement" ):
                listener.exitHelpStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelpStatement" ):
                return visitor.visitHelpStatement(self)
            else:
                return visitor.visitChildren(self)




    def helpStatement(self):

        localctx = SonicRPGParser.HelpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_helpStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(SonicRPGParser.HELP)
            self.state = 185
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(SonicRPGParser.MAP, 0)

        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_mapStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapStatement" ):
                listener.enterMapStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapStatement" ):
                listener.exitMapStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapStatement" ):
                return visitor.visitMapStatement(self)
            else:
                return visitor.visitChildren(self)




    def mapStatement(self):

        localctx = SonicRPGParser.MapStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mapStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(SonicRPGParser.MAP)
            self.state = 188
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SonicRPGParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(SonicRPGParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = SonicRPGParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.expression(0)
            self.state = 191
            self.match(SonicRPGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SonicRPGParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SonicRPGParser.ExpressionContext,i)


        def compareOp(self):
            return self.getTypedRuleContext(SonicRPGParser.CompareOpContext,0)


        def getRuleIndex(self):
            return SonicRPGParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = SonicRPGParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condition)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.expression(0)
                self.state = 194
                self.compareOp()
                self.state = 195
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(SonicRPGParser.GT, 0)

        def LT(self):
            return self.getToken(SonicRPGParser.LT, 0)

        def GTE(self):
            return self.getToken(SonicRPGParser.GTE, 0)

        def LTE(self):
            return self.getToken(SonicRPGParser.LTE, 0)

        def EQ(self):
            return self.getToken(SonicRPGParser.EQ, 0)

        def NEQ(self):
            return self.getToken(SonicRPGParser.NEQ, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_compareOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareOp" ):
                listener.enterCompareOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareOp" ):
                listener.exitCompareOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOp" ):
                return visitor.visitCompareOp(self)
            else:
                return visitor.visitChildren(self)




    def compareOp(self):

        localctx = SonicRPGParser.CompareOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_compareOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34634616274944) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SonicRPGParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SonicRPGParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SonicRPGParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(SonicRPGParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(SonicRPGParser.AtomContext,0)


        def MULTIPLY(self):
            return self.getToken(SonicRPGParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(SonicRPGParser.DIVIDE, 0)

        def PLUS(self):
            return self.getToken(SonicRPGParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SonicRPGParser.MINUS, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SonicRPGParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.state = 203
                self.match(SonicRPGParser.LPAREN)
                self.state = 204
                self.expression(0)
                self.state = 205
                self.match(SonicRPGParser.RPAREN)
                pass
            elif token in [1, 2, 3, 4, 5, 36, 37, 56, 57, 58]:
                self.state = 207
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 216
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = SonicRPGParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 210
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 211
                        _la = self._input.LA(1)
                        if not(_la==47 or _la==48):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 212
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = SonicRPGParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 213
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 214
                        _la = self._input.LA(1)
                        if not(_la==45 or _la==46):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 215
                        self.expression(4)
                        pass

             
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SonicRPGParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(SonicRPGParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(SonicRPGParser.IDENTIFIER, 0)

        def gameProperty(self):
            return self.getTypedRuleContext(SonicRPGParser.GamePropertyContext,0)


        def getRuleIndex(self):
            return SonicRPGParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = SonicRPGParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_atom)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(SonicRPGParser.NUMBER)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(SonicRPGParser.STRING)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.match(SonicRPGParser.IDENTIFIER)
                pass
            elif token in [1, 2, 3, 4, 5, 36, 37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.gameProperty()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GamePropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RINGS(self):
            return self.getToken(SonicRPGParser.RINGS, 0)

        def SPEED(self):
            return self.getToken(SonicRPGParser.SPEED, 0)

        def getRuleIndex(self):
            return SonicRPGParser.RULE_gameProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameProperty" ):
                listener.enterGameProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameProperty" ):
                listener.exitGameProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGameProperty" ):
                return visitor.visitGameProperty(self)
            else:
                return visitor.visitChildren(self)




    def gameProperty(self):

        localctx = SonicRPGParser.GamePropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_gameProperty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 206158430270) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




