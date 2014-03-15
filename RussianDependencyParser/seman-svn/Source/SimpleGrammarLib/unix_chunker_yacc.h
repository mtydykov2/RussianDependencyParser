/* A Bison parser, made by GNU Bison 2.7.12-4996.  */

/* Bison interface for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2013 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_UNIX_CHUNKER_YACC_TMP_HPP_INCLUDED
# define YY_YY_UNIX_CHUNKER_YACC_TMP_HPP_INCLUDED
/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 1
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     CHUNK_ATTRIB_VALUE = 258,
     CHUNK_WORD_FORM = 259,
     CHUNK_NAME = 260,
     CHUNK_RULE_PART_DELIM = 261,
     CHUNK_RULE_DELIM = 262,
     CHUNK_ATTR_ASSIGNMENT = 263,
     CHUNK_ATTR_EQU_CHAR = 264,
     CHUNK_ATTR_VARIABLE = 265,
     CHUNK_ATTR = 266,
     CHUNK_INCLUDE = 267,
     CHUNK_OR = 268,
     CHUNK_FACULTATIVE = 269
   };
#endif


#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{
/* Line 2053 of yacc.c  */
#line 26 "chunker.y"

const string*		m_LabelPtr;  
CChunkNode*			m_pNode;  
CNodeAttributes*	m_pAttributes;  
CNodeAttribute*		m_pAttribute;
CChunkRule*			m_pRule;  
CChunkGrammar*		m_pGrammar;  
CRuleFeature*		m_pRuleFeature;  


/* Line 2053 of yacc.c  */
#line 82 "unix_chunker_yacc_tmp.hpp"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif


#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */

#endif /* !YY_YY_UNIX_CHUNKER_YACC_TMP_HPP_INCLUDED  */
