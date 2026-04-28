# Generated from SonicRPG.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SonicRPGParser import SonicRPGParser
else:
    from SonicRPGParser import SonicRPGParser

# This class defines a complete listener for a parse tree produced by SonicRPGParser.
class SonicRPGListener(ParseTreeListener):

    # Enter a parse tree produced by SonicRPGParser#program.
    def enterProgram(self, ctx:SonicRPGParser.ProgramContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#program.
    def exitProgram(self, ctx:SonicRPGParser.ProgramContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#statement.
    def enterStatement(self, ctx:SonicRPGParser.StatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#statement.
    def exitStatement(self, ctx:SonicRPGParser.StatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#moveStatement.
    def enterMoveStatement(self, ctx:SonicRPGParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#moveStatement.
    def exitMoveStatement(self, ctx:SonicRPGParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#direction.
    def enterDirection(self, ctx:SonicRPGParser.DirectionContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#direction.
    def exitDirection(self, ctx:SonicRPGParser.DirectionContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#collectStatement.
    def enterCollectStatement(self, ctx:SonicRPGParser.CollectStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#collectStatement.
    def exitCollectStatement(self, ctx:SonicRPGParser.CollectStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#collectTarget.
    def enterCollectTarget(self, ctx:SonicRPGParser.CollectTargetContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#collectTarget.
    def exitCollectTarget(self, ctx:SonicRPGParser.CollectTargetContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#useStatement.
    def enterUseStatement(self, ctx:SonicRPGParser.UseStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#useStatement.
    def exitUseStatement(self, ctx:SonicRPGParser.UseStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#useTarget.
    def enterUseTarget(self, ctx:SonicRPGParser.UseTargetContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#useTarget.
    def exitUseTarget(self, ctx:SonicRPGParser.UseTargetContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#fightStatement.
    def enterFightStatement(self, ctx:SonicRPGParser.FightStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#fightStatement.
    def exitFightStatement(self, ctx:SonicRPGParser.FightStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#sayStatement.
    def enterSayStatement(self, ctx:SonicRPGParser.SayStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#sayStatement.
    def exitSayStatement(self, ctx:SonicRPGParser.SayStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#ifStatement.
    def enterIfStatement(self, ctx:SonicRPGParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#ifStatement.
    def exitIfStatement(self, ctx:SonicRPGParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#loopStatement.
    def enterLoopStatement(self, ctx:SonicRPGParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#loopStatement.
    def exitLoopStatement(self, ctx:SonicRPGParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#exitStatement.
    def enterExitStatement(self, ctx:SonicRPGParser.ExitStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#exitStatement.
    def exitExitStatement(self, ctx:SonicRPGParser.ExitStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#saveStatement.
    def enterSaveStatement(self, ctx:SonicRPGParser.SaveStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#saveStatement.
    def exitSaveStatement(self, ctx:SonicRPGParser.SaveStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#loadStatement.
    def enterLoadStatement(self, ctx:SonicRPGParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#loadStatement.
    def exitLoadStatement(self, ctx:SonicRPGParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#inventoryStatement.
    def enterInventoryStatement(self, ctx:SonicRPGParser.InventoryStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#inventoryStatement.
    def exitInventoryStatement(self, ctx:SonicRPGParser.InventoryStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#waitStatement.
    def enterWaitStatement(self, ctx:SonicRPGParser.WaitStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#waitStatement.
    def exitWaitStatement(self, ctx:SonicRPGParser.WaitStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#lookStatement.
    def enterLookStatement(self, ctx:SonicRPGParser.LookStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#lookStatement.
    def exitLookStatement(self, ctx:SonicRPGParser.LookStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#statusStatement.
    def enterStatusStatement(self, ctx:SonicRPGParser.StatusStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#statusStatement.
    def exitStatusStatement(self, ctx:SonicRPGParser.StatusStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#helpStatement.
    def enterHelpStatement(self, ctx:SonicRPGParser.HelpStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#helpStatement.
    def exitHelpStatement(self, ctx:SonicRPGParser.HelpStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#mapStatement.
    def enterMapStatement(self, ctx:SonicRPGParser.MapStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#mapStatement.
    def exitMapStatement(self, ctx:SonicRPGParser.MapStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SonicRPGParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SonicRPGParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#condition.
    def enterCondition(self, ctx:SonicRPGParser.ConditionContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#condition.
    def exitCondition(self, ctx:SonicRPGParser.ConditionContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#compareOp.
    def enterCompareOp(self, ctx:SonicRPGParser.CompareOpContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#compareOp.
    def exitCompareOp(self, ctx:SonicRPGParser.CompareOpContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#expression.
    def enterExpression(self, ctx:SonicRPGParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#expression.
    def exitExpression(self, ctx:SonicRPGParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#atom.
    def enterAtom(self, ctx:SonicRPGParser.AtomContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#atom.
    def exitAtom(self, ctx:SonicRPGParser.AtomContext):
        pass


    # Enter a parse tree produced by SonicRPGParser#gameProperty.
    def enterGameProperty(self, ctx:SonicRPGParser.GamePropertyContext):
        pass

    # Exit a parse tree produced by SonicRPGParser#gameProperty.
    def exitGameProperty(self, ctx:SonicRPGParser.GamePropertyContext):
        pass



del SonicRPGParser