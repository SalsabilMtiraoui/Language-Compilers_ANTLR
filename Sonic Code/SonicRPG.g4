grammar SonicRPG;

// ========== RÈGLES LEXICALES (TOKENS) ==========

// Mots-clés du jeu
MOVE        : 'MOVE' | 'move';
COLLECT     : 'COLLECT' | 'collect';
USE         : 'USE' | 'use';
TOKEN       : 'TOKEN' | 'token';
FIGHT       : 'FIGHT' | 'fight';
BOSS        : 'BOSS' | 'boss';
SAY         : 'SAY' | 'say';
IF          : 'IF' | 'if';
ELSE        : 'ELSE' | 'else';
ENDIF       : 'ENDIF' | 'endif';
LOOP        : 'LOOP' | 'loop';
ENDLOOP     : 'ENDLOOP' | 'endloop';
EXIT        : 'EXIT' | 'exit';
SAVE        : 'SAVE' | 'save';
LOAD        : 'LOAD' | 'load';
INVENTORY   : 'INVENTORY' | 'inventory';
WAIT        : 'WAIT' | 'wait';
STATUS      : 'STATUS' | 'status';
MAP         : 'MAP' | 'map';
HELP        : 'HELP' | 'help';

// Directions
UP      : 'UP' | 'up';
DOWN    : 'DOWN' | 'down';
LEFT    : 'LEFT' | 'left';
RIGHT   : 'RIGHT' | 'right';
NORTH   : 'NORTH' | 'north';
SOUTH   : 'SOUTH' | 'south';
EAST    : 'EAST' | 'east';
WEST    : 'WEST' | 'west';

// Objets
RING        : 'RING' | 'ring';
RINGS       : 'RINGS' | 'rings';
SPEED       : 'SPEED' | 'speed';
CHECKPOINT  : 'CHECKPOINT' | 'checkpoint';

// Opérateurs
GT   : '>';
LT   : '<';
GTE  : '>=';
LTE  : '<=';
EQ   : '==' | '=';
NEQ  : '!=' | '<>';

PLUS     : '+';
MINUS    : '-';
MULTIPLY : '*';
DIVIDE   : '/';

// Ponctuation
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
SEMICOLON   : ';';
COMMA       : ',';
DOT         : '.';

// Types de données
NUMBER      : [0-9]+;
STRING      : '"' (~["\r\n])* '"';
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;

// Espaces et commentaires
WS              : [ \t\r\n]+ -> skip;
COMMENT         : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip;

// ========== RÈGLES SYNTAXIQUES ==========

program     : statement* EOF;

// Instructions (une seule règle unifiée)
statement
    : moveStatement
    | collectStatement
    | useStatement
    | fightStatement
    | sayStatement
    | ifStatement
    | loopStatement
    | exitStatement
    | saveStatement
    | loadStatement
    | inventoryStatement
    | waitStatement
    | statusStatement
    | helpStatement
    | mapStatement
    | expressionStatement
    ;

// MOVE <direction> [NUMBER];
moveStatement : MOVE direction (NUMBER)? SEMICOLON;
direction     : UP | DOWN | LEFT | RIGHT | NORTH | SOUTH | EAST | WEST;

// COLLECT <target> [NUMBER];
collectStatement : COLLECT collectTarget (NUMBER)? SEMICOLON;
collectTarget    : RING | RINGS | TOKEN | IDENTIFIER;

// USE <target>;
useStatement : USE useTarget SEMICOLON;
useTarget    : TOKEN | SPEED | CHECKPOINT | IDENTIFIER;

// FIGHT BOSS;
fightStatement : FIGHT BOSS SEMICOLON;

// SAY "message";
sayStatement : SAY STRING SEMICOLON;

// IF (...) { ... } [ELSE { ... }] ENDIF;
ifStatement : IF LPAREN condition RPAREN LBRACE statement* RBRACE
              (ELSE LBRACE statement* RBRACE)?
              ENDIF SEMICOLON;

// LOOP [NUMBER] { ... } ENDLOOP;
loopStatement : LOOP (NUMBER)? LBRACE statement* RBRACE ENDLOOP SEMICOLON;

// EXIT;
exitStatement : EXIT SEMICOLON;

// LOAD ["nom"];
loadStatement : LOAD (STRING)? SEMICOLON;

// INVENTORY;
inventoryStatement : INVENTORY SEMICOLON;

// WAIT [NUMBER];
waitStatement : WAIT (NUMBER)? SEMICOLON;

// STATUS;
statusStatement : STATUS SEMICOLON;

// HELP;
helpStatement : HELP SEMICOLON;

// MAP;
mapStatement : MAP SEMICOLON;

// expression;
expressionStatement : expression SEMICOLON;

// condition pour IF
condition : expression compareOp expression
          | expression
          ;

compareOp : GT | LT | GTE | LTE | EQ | NEQ;

// expression arithmétique
expression : expression (MULTIPLY | DIVIDE) expression
           | expression (PLUS | MINUS) expression
           | LPAREN expression RPAREN
           | atom
           ;

atom : NUMBER
     | STRING
     | IDENTIFIER
     | gameProperty
     ;

// Variables internes du jeu accessibles
gameProperty : RINGS
             | SPEED
             | 'position'
             | 'x'
             | 'y'
             | 'boss_unlocked'
             | 'game_over'
             ;
