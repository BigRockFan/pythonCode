#Rohan P
#2/21/2018
#putcha.py
#self portrait
from graphics import *

win = GraphWin("Self Portrait", 500, 500)
skincolor = color_rgb(255, 170, 153)
otherskin = color_rgb(204, 128, 102)
    
win.setBackground(color_rgb(102, 128, 102))

face = Polygon(Point(  238 ,  225 ), 
Point(  226 ,  224 ), 
Point(  217 ,  218 ), 
Point(  209 ,  212 ), 
Point(  201 ,  204 ), 
Point(  196 ,  198 ), 
Point(  192 ,  190 ), 
Point(  192 ,  178 ), 
Point(  188 ,  163 ), 
Point(  188 ,  151 ), 
Point(  188 ,  140 ), 
Point(  181 ,  128 ), 
Point(  185 ,  117 ), 
Point(  185 ,  108 ), 
Point(  186 ,  98 ), 
Point(  192 ,  91 ), 
Point(  202 ,  85 ), 
Point(  212 ,  82 ), 
Point(  226 ,  80 ), 
Point(  237 ,  77 ), 
Point(  249 ,  78 ), 
Point(  262 ,  80 ), 
Point(  271 ,  82 ), 
Point(  278 ,  90 ), 
Point(  281 ,  102 ), 
Point(  282 ,  111 ), 
Point(  285 ,  124 ), 
Point(  290 ,  137 ), 
Point(  287 ,  151 ), 
Point(  284 ,  169 ), 
Point(  279 ,  184 ), 
Point(  271 ,  200 ), 
Point(  263 ,  211 ), 
Point(  254 ,  218 ))
face.setFill(skincolor)
face.setOutline(skincolor)
face.draw(win)

eye1 = Polygon(Point(  195 ,  144 ), 
Point(  198 ,  141 ), 
Point(  201 ,  138 ), 
Point(  206 ,  137 ), 
Point(  211 ,  137 ),  
Point(  215 ,  141 ), 
Point(  212 ,  142 ), 
Point(  205 ,  142 ))
eye1.setFill("white")
eye1.setWidth(0)
eye1.draw(win)

eye2 = Polygon(Point(  241 ,  138 ), 
Point(  244 ,  135 ), 
Point(  252 ,  133 ), 
Point(  259 ,  134 ), 
Point(  265 ,  136 ), 
Point(  261 ,  138 ), 
Point(  255 ,  138 ), 
Point(  250 ,  138 ))
eye2.setFill("white")
eye2.setWidth(0)
eye2.draw(win)

leftear = Polygon(Point(  287 ,  148 ), 
Point(  287 ,  143 ), 
Point(  292 ,  137 ), 
Point(  297 ,  135 ), 
Point(  303 ,  136 ), 
Point(  307 ,  140 ), 
Point(  309 ,  147 ), 
Point(  306 ,  155 ), 
Point(  304 ,  166 ), 
Point(  302 ,  169 ), 
Point(  299 ,  174 ), 
Point(  295 ,  181 ), 
Point(  290 ,  182 ), 
Point(  286 ,  180 ), 
Point(  284 ,  176 ), 
Point(  284 ,  164 ))
leftear.setFill(skincolor)
leftear.setOutline(skincolor)
leftear.draw(win)

rightear = Polygon(Point(  194 ,  179 ), 
Point(  190 ,  178 ), 
Point(  188 ,  174 ), 
Point(  186 ,  171 ), 
Point(  184 ,  166 ), 
Point(  181 ,  159 ), 
Point(  179 ,  156 ), 
Point(  178 ,  152 ), 
Point(  178 ,  151 ), 
Point(  179 ,  149 ), 
Point(  179 ,  143 ), 
Point(  181 ,  139 ), 
Point(  185 ,  138 ), 
Point(  188 ,  139 ))
rightear.setFill(skincolor)
rightear.setOutline(skincolor)
rightear.draw(win)

hair = Polygon(Point(  186 ,  136 ), 
Point(  182 ,  137 ), 
Point(  180 ,  124 ), 
Point(  179 ,  111 ), 
Point(  179 ,  106 ), 
Point(  177 ,  105 ), 
Point(  171 ,  97 ), 
Point(  169 ,  85 ), 
Point(  170 ,  72 ), 
Point(  172 ,  62 ), 
Point(  179 ,  56 ), 
Point(  191 ,  46 ), 
Point(  205 ,  39 ), 
Point(  219 ,  37 ), 
Point(  238 ,  38 ), 
Point(  251 ,  38 ), 
Point(  265 ,  39 ), 
Point(  277 ,  44 ), 
Point(  286 ,  54 ), 
Point(  294 ,  63 ), 
Point(  300 ,  73 ), 
Point(  300 ,  84 ), 
Point(  304 ,  101 ), 
Point(  306 ,  113 ), 
Point(  306 ,  128 ), 
Point(  304 ,  135 ), 
Point(  299 ,  135 ), 
Point(  293 ,  144 ), 
Point(  290 ,  144 ), 
Point(  289 ,  130 ), 
Point(  284 ,  124 ), 
Point(  280 ,  119 ), 
Point(  276 ,  103 ), 
Point(  275 ,  91 ), 
Point(  264 ,  85 ), 
Point(  251 ,  82 ), 
Point(  240 ,  83 ), 
Point(  226 ,  84 ), 
Point(  203 ,  89 ), 
Point(  192 ,  94 ), 
Point(  187 ,  102 ), 
Point(  184 ,  112 ), 
Point(  183 ,  121 ), 
Point(  186 ,  130 ))
hair.setFill("black")
hair.draw(win)

nose = Polygon(Point(  220 ,  137 ), 
Point(  220 ,  142 ), 
Point(  218 ,  148 ), 
Point(  217 ,  155 ), 
Point(  215 ,  160 ), 
Point(  213 ,  165 ), 
Point(  216 ,  167 ), 
Point(  221 ,  168 ), 
Point(  225 ,  170 ), 
Point(  230 ,  170 ), 
Point(  234 ,  166 ), 
Point(  238 ,  164 ), 
Point(  243 ,  164 ), 
Point(  245 ,  161 ), 
Point(  243 ,  158 ), 
Point(  239 ,  156 ), 
Point(  234 ,  148 ), 
Point(  232 ,  142 ), 
Point(  230 ,  137 ), 
Point(  228 ,  136 ), 
Point(  224 ,  136 ))
nose.setFill(skincolor)
nose.setOutline(color_rgb(153, 85, 51))
nose.draw(win)

mouth = Polygon(Point(  220 ,  180 ), 
Point(  228 ,  181 ), 
Point(  234 ,  181 ), 
Point(  237 ,  181 ), 
Point(  244 ,  180 ), 
Point(  249 ,  180 ), 
Point(  257 ,  180 ), 
Point(  259 ,  183 ), 
Point(  252 ,  185 ), 
Point(  249 ,  186 ), 
Point(  245 ,  187 ), 
Point(  242 ,  188 ), 
Point(  239 ,  189 ), 
Point(  237 ,  190 ), 
Point(  233 ,  190 ), 
Point(  228 ,  190 ), 
Point(  224 ,  190 ), 
Point(  218 ,  190 ), 
Point(  216 ,  190 ), 
Point(  214 ,  188 ), 
Point(  212 ,  186 ), 
Point(  214 ,  184 ))
mouth.setOutline(color_rgb(250, 128, 153))
mouth.setWidth(3)
mouth.draw(win)

mouthside1 = Polygon(Point(  218 ,  183 ), 
Point(  216 ,  185 ), 
Point(  214 ,  187 ), 
Point(  215 ,  188 ), 
Point(  217 ,  188 ), 
Point(  217 ,  186 ), 
Point(  218 ,  184 ))
mouthside1.setFill(color_rgb(50, 0, 0))
mouthside1.draw(win)

mouthside2 = Polygon(Point(  253 ,  181 ), 
Point(  255 ,  180 ), 
Point(  258 ,  180 ), 
Point(  257 ,  182 ), 
Point(  254 ,  183 ))
mouthside2.setFill(color_rgb(50, 0, 0))
mouthside2.draw(win)

eyebrow1 = Polygon(Point(  189 ,  130 ), 
Point(  189 ,  128 ), 
Point(  190 ,  124 ), 
Point(  194 ,  122 ), 
Point(  199 ,  121 ), 
Point(  203 ,  121 ), 
Point(  208 ,  122 ), 
Point(  212 ,  123 ), 
Point(  213 ,  126 ), 
Point(  210 ,  126 ), 
Point(  207 ,  126 ), 
Point(  204 ,  126 ), 
Point(  200 ,  127 ), 
Point(  195 ,  127 ), 
Point(  192 ,  128 ))
eyebrow1.setFill("black")
eyebrow1.draw(win)

eyebrow2 = Polygon(Point(  238 ,  120 ), 
Point(  242 ,  120 ), 
Point(  247 ,  118 ), 
Point(  251 ,  118 ), 
Point(  256 ,  118 ), 
Point(  260 ,  118 ), 
Point(  264 ,  119 ), 
Point(  264 ,  121 ), 
Point(  261 ,  121 ), 
Point(  258 ,  121 ), 
Point(  253 ,  123 ), 
Point(  248 ,  123 ), 
Point(  246 ,  123 ), 
Point(  243 ,  122 ), 
Point(  240 ,  122 ))
eyebrow2.setFill("black")
eyebrow2.draw(win)

iris1 = Polygon(Point(  202 ,  139 ), 
Point(  202 ,  141 ), 
Point(  210 ,  141 ), 
Point(  210 ,  137 ))
iris1.setFill(color_rgb(40, 26, 13))
iris1.draw(win)

iris2 = Polygon(Point(  249 ,  134 ), 
Point(  248 ,  136 ), 
Point(  249 ,  137 ), 
Point(  258 ,  137 ), 
Point(  259 ,  134 ))
iris2.setFill(color_rgb(40, 26, 13))
iris2.draw(win)

neck = Polygon(Point(  208 ,  212 ), 
Point(  209 ,  220 ), 
Point(  209 ,  228 ), 
Point(  210 ,  236 ), 
Point(  211 ,  246 ), 
Point(  214 ,  251 ), 
Point(  214 ,  257 ), 
Point(  216 ,  264 ), 
Point(  220 ,  269 ), 
Point(  225 ,  271 ), 
Point(  229 ,  274 ), 
Point(  233 ,  278 ), 
Point(  235 ,  285 ), 
Point(  239 ,  289 ), 
Point(  242 ,  295 ), 
Point(  245 ,  291 ), 
Point(  249 ,  288 ), 
Point(  255 ,  283 ), 
Point(  262 ,  277 ), 
Point(  271 ,  272 ), 
Point(  279 ,  266 ), 
Point(  285 ,  262 ), 
Point(  293 ,  256 ), 
Point(  299 ,  249 ), 
Point(  303 ,  244 ), 
Point(  304 ,  241 ), 
Point(  303 ,  235 ), 
Point(  301 ,  230 ), 
Point(  299 ,  225 ), 
Point(  297 ,  219 ), 
Point(  296 ,  213 ),  
Point(  291 ,  207 ), 
Point(  287 ,  200 ), 
Point(  282 ,  193 ), 
Point(  279 ,  186 ), 
Point(  276 ,  190 ), 
Point(  273 ,  196 ), 
Point(  269 ,  202 ), 
Point(  264 ,  209 ), 
Point(  260 ,  213 ), 
Point(  254 ,  217 ), 
Point(  245 ,  219 ), 
Point(  235 ,  217 ), 
Point(  223 ,  213 ), 
Point(  215 ,  210 ))
neck.setFill(skincolor)
neck.setOutline(skincolor)
neck.draw(win)

jacketright1 = Polygon(Point(  205 ,  500 ), 
Point(  206 ,  490 ), 
Point(  206 ,  482 ), 
Point(  207 ,  474 ), 
Point(  208 ,  465 ), 
Point(  210 ,  458 ), 
Point(  211 ,  439 ), 
Point(  214 ,  422 ), 
Point(  216 ,  407 ), 
Point(  217 ,  395 ), 
Point(  218 ,  381 ), 
Point(  221 ,  370 ), 
Point(  222 ,  361 ), 
Point(  223 ,  350 ), 
Point(  224 ,  342 ), 
Point(  228 ,  332 ), 
Point(  229 ,  325 ), 
Point(  233 ,  317 ), 
Point(  237 ,  307 ), 
Point(  240 ,  299 ), 
Point(  243 ,  296 ), 
Point(  245 ,  293 ), 
Point(  248 ,  289 ), 
Point(  252 ,  284 ), 
Point(  259 ,  279 ), 
Point(  266 ,  275 ), 
Point(  273 ,  271 ), 
Point(  281 ,  265 ), 
Point(  290 ,  265 ), 
Point(  298 ,  267 ), 
Point(  309 ,  269 ), 
Point(  318 ,  270 ), 
Point(  330 ,  271 ), 
Point(  339 ,  271 ), 
Point(  349 ,  271 ), 
Point(  357 ,  271 ), 
Point(  365 ,  271 ), 
Point(  371 ,  270 ), 
Point(  378 ,  274 ), 
Point(  387 ,  280 ), 
Point(  395 ,  286 ), 
Point(  402 ,  290 ), 
Point(  410 ,  297 ), 
Point(  415 ,  303 ), 
Point(  421 ,  313 ), 
Point(  426 ,  321 ), 
Point(  431 ,  330 ), 
Point(  438 ,  346 ), 
Point(  442 ,  362 ), 
Point(  445 ,  383 ), 
Point(  448 ,  402 ), 
Point(  450 ,  428 ), 
Point(  451 ,  449 ), 
Point(  453 ,  466 ), 
Point(  453 ,  486 ), 
Point(  453 ,  500 ))
jacketright1.setFill(color_rgb(33, 39, 53))
jacketright1.draw(win)

jacketleft1 = Polygon(Point(  205 ,  500 ), 
Point(  206 ,  497 ), 
Point(  207 ,  474 ), 
Point(  209 ,  461 ), 
Point(  211 ,  450 ), 
Point(  213 ,  438 ), 
Point(  215 ,  420 ), 
Point(  215 ,  407 ), 
Point(  216 ,  396 ), 
Point(  220 ,  381 ), 
Point(  221 ,  368 ), 
Point(  224 ,  352 ), 
Point(  225 ,  340 ), 
Point(  226 ,  328 ), 
Point(  224 ,  314 ), 
Point(  222 ,  303 ), 
Point(  220 ,  294 ), 
Point(  218 ,  288 ), 
Point(  212 ,  279 ), 
Point(  207 ,  272 ), 
Point(  204 ,  266 ), 
Point(  200 ,  253 ), 
Point(  198 ,  245 ), 
Point(  198 ,  240 ), 
Point(  193 ,  240 ), 
Point(  193 ,  248 ), 
Point(  188 ,  254 ), 
Point(  177 ,  259 ), 
Point(  161 ,  267 ), 
Point(  147 ,  277 ), 
Point(  135 ,  288 ), 
Point(  124 ,  306 ), 
Point(  117 ,  327 ), 
Point(  112 ,  351 ), 
Point(  108 ,  379 ),
Point(  105 ,  409 ), 
Point(  100 ,  443 ), 
Point(  95 ,  469 ), 
Point(  89 ,  500 ), 
Point(  88 ,  500 ))
jacketleft1.setFill(color_rgb(33, 39, 53))
jacketleft1.draw(win)

hood = Polygon(Point(  278 ,  269 ), 
Point(  282 ,  269 ), 
Point(  287 ,  269 ), 
Point(  293 ,  269 ), 
Point(  300 ,  270 ), 
Point(  306 ,  270 ), 
Point(  313 ,  271 ), 
Point(  319 ,  271 ), 
Point(  326 ,  272 ), 
Point(  336 ,  273 ), 
Point(  346 ,  273 ), 
Point(  355 ,  272 ), 
Point(  362 ,  271 ), 
Point(  371 ,  269 ), 
Point(  375 ,  271 ), 
Point(  379 ,  275 ), 
Point(  382 ,  270 ), 
Point(  386 ,  268 ), 
Point(  389 ,  264 ), 
Point(  392 ,  259 ), 
Point(  389 ,  255 ), 
Point(  383 ,  252 ), 
Point(  379 ,  253 ), 
Point(  373 ,  253 ), 
Point(  368 ,  255 ), 
Point(  364 ,  253 ), 
Point(  359 ,  253 ), 
Point(  358 ,  247 ), 
Point(  353 ,  241 ), 
Point(  347 ,  236 ), 
Point(  342 ,  230 ), 
Point(  335 ,  225 ), 
Point(  333 ,  220 ), 
Point(  329 ,  216 ), 
Point(  323 ,  212 ), 
Point(  318 ,  209 ), 
Point(  312 ,  207 ), 
Point(  306 ,  207 ), 
Point(  299 ,  207 ), 
Point(  295 ,  210 ), 
Point(  295 ,  216 ), 
Point(  297 ,  222 ), 
Point(  300 ,  230 ), 
Point(  302 ,  234 ), 
Point(  304 ,  240 ), 
Point(  302 ,  245 ), 
Point(  299 ,  250 ), 
Point(  294 ,  254 ), 
Point(  288 ,  258 ), 
Point(  282 ,  265 ))
hood.setFill(color_rgb(102, 85, 102))
hood.setOutline(color_rgb(102, 85, 102))
hood.draw(win)

hoodhole = Polygon(Point(  373 ,  257 ), 
Point(  378 ,  257 ), 
Point(  383 ,  257 ), 
Point(  384 ,  260 ), 
Point(  379 ,  263 ), 
Point(  376 ,  264 ), 
Point(  373 ,  260 ), 
Point(  372 ,  258 ))
hoodhole.setFill(color_rgb(51, 43, 51))
hoodhole.setOutline(color_rgb(71, 63, 71))
hoodhole.draw(win)

hoodleft = Polygon(Point(  212 ,  248 ), 
Point(  210 ,  255 ), 
Point(  208 ,  261 ), 
Point(  207 ,  267 ), 
Point(  204 ,  265 ), 
Point(  203 ,  260 ), 
Point(  201 ,  254 ), 
Point(  198 ,  248 ), 
Point(  198 ,  241 ), 
Point(  197 ,  238 ), 
Point(  197 ,  235 ), 
Point(  200 ,  230 ), 
Point(  201 ,  225 ), 
Point(  205 ,  220 ), 
Point(  209 ,  218 ), 
Point(  209 ,  225 ), 
Point(  210 ,  231 ), 
Point(  210 ,  239 ), 
Point(  210 ,  243 ))
hoodleft.setOutline(color_rgb(102, 85, 102))
hoodleft.setFill(color_rgb(102, 85, 102))
hoodleft.draw(win)

shirtcollar = Polygon(Point(  212 ,  248 ), 
Point(  211 ,  251 ), 
Point(  209 ,  254 ), 
Point(  209 ,  259 ), 
Point(  207 ,  264 ), 
Point(  205 ,  267 ), 
Point(  206 ,  270 ), 
Point(  206 ,  273 ), 
Point(  210 ,  275 ), 
Point(  213 ,  277 ), 
Point(  217 ,  277 ), 
Point(  222 ,  277 ), 
Point(  226 ,  276 ), 
Point(  232 ,  278 ), 
Point(  230 ,  274 ), 
Point(  225 ,  271 ), 
Point(  220 ,  269 ), 
Point(  217 ,  266 ), 
Point(  216 ,  261 ), 
Point(  214 ,  255 ), 
Point(  214 ,  251 ))
shirtcollar.setFill(color_rgb(153, 170, 204))
shirtcollar.setOutline(color_rgb(153, 170, 204))
shirtcollar.draw(win)

shirt = Polygon(Point(  211 ,  278 ), 
Point(  213 ,  277 ), 
Point(  218 ,  277 ), 
Point(  223 ,  276 ), 
Point(  226 ,  274 ), 
Point(  229 ,  276 ), 
Point(  234 ,  281 ), 
Point(  237 ,  284 ), 
Point(  240 ,  289 ), 
Point(  243 ,  292 ), 
Point(  242 ,  297 ), 
Point(  239 ,  302 ), 
Point(  237 ,  307 ), 
Point(  235 ,  312 ), 
Point(  233 ,  316 ), 
Point(  230 ,  316 ), 
Point(  226 ,  316 ), 
Point(  226 ,  312 ), 
Point(  225 ,  309 ), 
Point(  222 ,  305 ), 
Point(  220 ,  300 ), 
Point(  219 ,  294 ), 
Point(  218 ,  292 ), 
Point(  216 ,  287 ), 
Point(  214 ,  283 ), 
Point(  213 ,  280 ))
shirt.setFill(color_rgb(0, 0, 140))
shirt.setOutline(color_rgb(0, 0, 140))
shirt.draw(win)

zipper = Polygon(Point(  223 ,  307 ), 
Point(  223 ,  313 ), 
Point(  225 ,  319 ), 
Point(  226 ,  325 ), 
Point(  225 ,  332 ), 
Point(  226 ,  336 ), 
Point(  228 ,  332 ), 
Point(  228 ,  328 ), 
Point(  230 ,  323 ), 
Point(  231 ,  320 ), 
Point(  233 ,  317 ), 
Point(  230 ,  317 ), 
Point(  227 ,  317 ), 
Point(  226 ,  317 ), 
Point(  226 ,  314 ), 
Point(  225 ,  310 ))
zipper.setFill("black")
zipper.draw(win)

nosecover = Polygon(Point(  217 ,  134 ), 
Point(  215 ,  148 ), 
Point(  226 ,  148 ), 
Point(  239 ,  148 ), 
Point(  230 ,  131 ))
nosecover.setOutline(skincolor)
nosecover.setFill(skincolor)
nosecover.draw(win)

teeth = Polygon(Point(  218 ,  184 ), 
Point(  218 ,  186 ), 
Point(  218 ,  189 ), 
Point(  220 ,  189 ), 
Point(  222 ,  189 ), 
Point(  225 ,  189 ), 
Point(  227 ,  189 ), 
Point(  231 ,  189 ), 
Point(  234 ,  189 ), 
Point(  238 ,  188 ), 
Point(  242 ,  187 ), 
Point(  246 ,  186 ), 
Point(  251 ,  185 ), 
Point(  253 ,  184 ), 
Point(  253 ,  181 ), 
Point(  251 ,  182 ), 
Point(  249 ,  182 ), 
Point(  244 ,  182 ), 
Point(  236 ,  182 ), 
Point(  230 ,  182 ), 
Point(  224 ,  182 ), 
Point(  220 ,  182 ), 
Point(  219 ,  184 ), 
Point(  219 ,  185 ))
teeth.setFill("white")
teeth.draw(win)

chin = Polygon(
Point(  209 ,  212 ), 
Point(  215 ,  217 ), 
Point(  222 ,  221 ), 
Point(  227 ,  224 ), 
Point(  232 ,  224 ), 
Point(  236 ,  224 ), 
Point(  241 ,  224 ), 
Point(  246 ,  221 ), 
Point(  252 ,  219 ), 
Point(  258 ,  214 ), 
Point(  263 ,  210 ), 
Point(  268 ,  204 ), 
Point(  279 ,  183 ),
Point(  279 ,  183 ),
Point(  268 ,  204 ),
Point(  263 ,  210 ),
Point(  258 ,  214 ),
Point(  252 ,  219 ),
Point(  246 ,  221 ),
Point(  241 ,  224 ),
Point(  236 ,  224 ),
Point(  232 ,  224 ),
Point(  227 ,  224 ),
Point(  222 ,  221 ),
Point(  215 ,  217 ),
Point(  209 ,  212 ))
chin.setOutline(color_rgb(153, 85, 51))
chin.draw(win)

chinblack = Polygon(
Point(  222 ,  221 ), 
Point(  227 ,  224 ), 
Point(  232 ,  224 ), 
Point(  236 ,  224 ), 
Point(  241 ,  224 ), 
Point(  246 ,  221 ), 
Point(  252 ,  219 ), 
Point(  258 ,  214 ), 
Point(  258 ,  214 ),
Point(  252 ,  219 ),
Point(  246 ,  221 ),
Point(  241 ,  224 ),
Point(  236 ,  224 ),
Point(  232 ,  224 ),
Point(  227 ,  224 ),
Point(  222 ,  221 ))
chinblack.setWidth(1)
chinblack.setFill(color_rgb(51, 43, 51))
chinblack.draw(win)

earshadow = Polygon(Point(  186 ,  136 ), 
Point(  187 ,  148 ), 
Point(  189 ,  161 ), 
Point(  190 ,  178 ), 
Point(  189 ,  161 ), 
Point(  187 ,  148 ), 
Point(  186 ,  136 ))
earshadow.setOutline(otherskin)
earshadow.draw(win)

lefteardetail = Polygon(Point(  186 ,  140 ), 
Point(  183 ,  143 ), 
Point(  183 ,  148 ), 
Point(  184 ,  158 ),
Point(  187 ,  165 ),                        
Point(  184 ,  158 ),                        
Point(  183 ,  148 ),
Point(  183 ,  143 ),
Point(  186 ,  140 ))                        
lefteardetail.setOutline(otherskin)
lefteardetail.setWidth(2)
lefteardetail.draw(win)

leftglass = Polygon(Point(  175 ,  140 ), 
Point(  176 ,  144 ), 
Point(  178 ,  149 ), 
Point(  180 ,  154 ), 
Point(  182 ,  158 ), 
Point(  185 ,  160 ), 
Point(  190 ,  162 ), 
Point(  195 ,  162 ), 
Point(  200 ,  161 ), 
Point(  205 ,  160 ), 
Point(  211 ,  158 ), 
Point(  216 ,  156 ), 
Point(  218 ,  147 ), 
Point(  218 ,  138 ), 
Point(  216 ,  135 ), 
Point(  211 ,  134 ), 
Point(  206 ,  134 ), 
Point(  195 ,  134 ), 
Point(  188 ,  136 ), 
Point(  182 ,  137 ))
leftglass.setOutline(color_rgb(51, 43, 51))
leftglass.setWidth(2)
leftglass.draw(win)

rightglass = Polygon(Point(  231 ,  135 ), 
Point(  232 ,  142 ), 
Point(  235 ,  149 ), 
Point(  239 ,  153 ), 
Point(  247 ,  155 ), 
Point(  256 ,  155 ), 
Point(  266 ,  154 ), 
Point(  272 ,  151 ), 
Point(  275 ,  144 ), 
Point(  275 ,  135 ), 
Point(  275 ,  129 ), 
Point(  271 ,  128 ), 
Point(  264 ,  128 ), 
Point(  256 ,  128 ), 
Point(  246 ,  129 ), 
Point(  237 ,  131 ))
rightglass.setOutline(color_rgb(51, 43, 51))
rightglass.setWidth(2)
rightglass.draw(win)

middleglass = Polygon(Point(  216 ,  135 ), 
Point(  225 ,  135 ), 
Point(  233 ,  134 ))
middleglass.setOutline(color_rgb(51, 43, 51))
middleglass.setWidth(3)
middleglass.draw(win)

rightglass_line = Polygon(Point(  275 ,  129 ), 
Point(  281 ,  129 ), 
Point(  286 ,  130 ), 
Point(  292 ,  132 ), 
Point(  300 ,  133 ),
Point(  303 ,  134 ))
rightglass_line.setOutline(color_rgb(51, 43, 51))
rightglass_line.setWidth(2)
rightglass_line.draw(win)

leftglass_line = Polygon(Point(  175 ,  139 ), 
Point(  181 ,  135 ))
leftglass_line.setOutline(color_rgb(51, 43, 51))
leftglass_line.setWidth(2)
leftglass_line.draw(win)

rightnostril = Polygon(Point(  234 ,  166 ), 
Point(  240 ,  165 ))
rightnostril.setFill("black")
rightnostril.draw(win)

righteardetail1 = Polygon(Point(  296 ,  147 ), 
Point(  294 ,  151 ), 
Point(  297 ,  157 ), 
Point(  295 ,  162 ), 
Point(  297 ,  157 ), 
Point(  294 ,  151 ), 
Point(  296 ,  147 ))
righteardetail1.setOutline(otherskin)
righteardetail1.setWidth(2)
righteardetail1.draw(win)

righteardetail2 = Polygon(Point(  297 ,  141 ), 
Point(  300 ,  139 ), 
Point(  303 ,  141 ), 
Point(  305 ,  146 ),
Point(  303 ,  152 ), 
Point(  300 ,  166 ),
Point(  303 ,  152 ),
Point(  305 ,  146 ),
Point(  303 ,  141 ),
Point(  300 ,  139 ),
Point(  297 ,  141 ))                          
righteardetail2.setOutline(otherskin)
righteardetail2.setWidth(2)
righteardetail2.draw(win)

jacketrightline = Polygon(Point(  378 ,  387 ), 
Point(  376 ,  411 ), 
Point(  370 ,  452 ), 
Point(  366 ,  498 ),
Point(  370 ,  452 ),
Point(  376 ,  411 ),
Point(  378 ,  387 ))
jacketrightline.draw(win)

jacketleftline = Polygon(Point(  137 ,  360 ), 
Point(  136 ,  403 ), 
Point(  135 ,  445 ), 
Point(  134 ,  499 ),
Point(  135 ,  445 ),
Point(  136 ,  403 ),
Point(  137 ,  360 ))
jacketleftline.draw(win)

name = Text(Point(250, 18), "Rohan Putcha")
name.setStyle("bold")
name.setSize(20)
name.draw(win)


