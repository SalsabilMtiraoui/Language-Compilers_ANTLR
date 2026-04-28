# Generated from SonicRPG.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SonicRPGParser import SonicRPGParser
else:
    from SonicRPGParser import SonicRPGParser

# This class defines a complete generic visitor for a parse tree produced by SonicRPGParser.

class SonicRPGVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SonicRPGParser#program.
    def visitProgram(self, ctx:SonicRPGParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#statement.
    def visitStatement(self, ctx:SonicRPGParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#moveStatement.
    def visitMoveStatement(self, ctx:SonicRPGParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#direction.
    def visitDirection(self, ctx:SonicRPGParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#collectStatement.
    def visitCollectStatement(self, ctx:SonicRPGParser.CollectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#collectTarget.
    def visitCollectTarget(self, ctx:SonicRPGParser.CollectTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#useStatement.
    def visitUseStatement(self, ctx:SonicRPGParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#useTarget.
    def visitUseTarget(self, ctx:SonicRPGParser.UseTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#fightStatement.
    def visitFightStatement(self, ctx:SonicRPGParser.FightStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#sayStatement.
    def visitSayStatement(self, ctx:SonicRPGParser.SayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#ifStatement.
    def visitIfStatement(self, ctx:SonicRPGParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#loopStatement.
    def visitLoopStatement(self, ctx:SonicRPGParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#exitStatement.
    def visitExitStatement(self, ctx:SonicRPGParser.ExitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#saveStatement.
    def visitSaveStatement(self, ctx:SonicRPGParser.SaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#loadStatement.
    def visitLoadStatement(self, ctx:SonicRPGParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#inventoryStatement.
    def visitInventoryStatement(self, ctx:SonicRPGParser.InventoryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#waitStatement.
    def visitWaitStatement(self, ctx:SonicRPGParser.WaitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#lookStatement.
    def visitLookStatement(self, ctx:SonicRPGParser.LookStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#statusStatement.
    def visitStatusStatement(self, ctx:SonicRPGParser.StatusStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#helpStatement.
    def visitHelpStatement(self, ctx:SonicRPGParser.HelpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#mapStatement.
    def visitMapStatement(self, ctx:SonicRPGParser.MapStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#expressionStatement.
    def visitExpressionStatement(self, ctx:SonicRPGParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#condition.
    def visitCondition(self, ctx:SonicRPGParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#compareOp.
    def visitCompareOp(self, ctx:SonicRPGParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#expression.
    def visitExpression(self, ctx:SonicRPGParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#atom.
    def visitAtom(self, ctx:SonicRPGParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SonicRPGParser#gameProperty.
    def visitGameProperty(self, ctx:SonicRPGParser.GamePropertyContext):
        return self.visitChildren(ctx)



del SonicRPGParser