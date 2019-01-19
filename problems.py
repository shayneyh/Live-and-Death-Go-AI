import goGame_main as goMain
import goGameClass as go


def generateTuples(string):
    list = []
    for i in range(0,len(string), 2):
        list.append((int(string[i]),int(string[i+1])))
    return list

def getProblems(ind):
    return problems[ind]

problems = []

# dpiecestest = generateTuples('01112122232414150503')
# # white
# apiecestest = generateTuples('00102030313233343525261606')
# dimstest = (7,7)
# availstest = generateTuples('02121304')
# eyeSpotstest = generateTuples('02121304')
# gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
# gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
# goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
# problems.append(goObject)
# go.GoGame.utility(goObject,'Def')

#Easy 4
# dpiecestest = [(0,0), (0, 3), (1, 2), (2, 2), (3, 1), (2, 0)]
# # white
# apiecestest = [(1,1),(0, 2), (1, 3), (2, 3), (3,3), (3, 2), (4,1), (5,2), (1, 5)]
# dimstest = (7,7)
# availstest = generateTuples('01102130405004')
# eyeSpotstest = generateTuples('0001101120210230')
dpiecestest = [(0, 3), (1, 2), (2, 2), (3, 1), (2, 0)]
# white
apiecestest = [(0, 2), (1, 3), (2, 3), (3,3), (3, 2), (4,1), (5,2), (1, 5)]
dimstest = (7,7)
availstest = generateTuples('001101102130405004')
eyeSpotstest = generateTuples('0001101120210230')
gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
problems.append(goObject)
go.GoGame.utility(goObject,'Def')

#Easy 5
dpiecestest = generateTuples('12223141')
# white
apiecestest = generateTuples('15132332425162')
dimstest = (7,6)
availstest = generateTuples('00011011212030405060030405')
eyeSpotstest = generateTuples('00011011202130')
gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
problems.append(goObject)
go.GoGame.utility(goObject,'Def')

# #Easy 9
# dpiecestest = generateTuples('011112404142')
# # white
# apiecestest = generateTuples('2002131433345051525354')
# dimstest = (7,6)
# availstest = generateTuples('00103021312232')
# eyeSpotstest = generateTuples('0010203010112131')
# gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
# gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
# goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
# problems.append(goObject)
# go.GoGame.utility(goObject,'Def')

#Easy 13
dpiecestest = generateTuples('122223242526161707')
# white
apiecestest = generateTuples('02112132333435472728181415')
dimstest = (5,10)
availstest = generateTuples('00010304050608091336')
eyeSpotstest = generateTuples('03040506131415')
gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
problems.append(goObject)
go.GoGame.utility(goObject,'Def')

#Easy 18
dpiecestest = generateTuples('01202122232414')
# white
apiecestest = generateTuples('10130431323334352515')
dimstest = (5,7)
availstest = generateTuples('0002030506111230')
eyeSpotstest = generateTuples('0001020310111213')
gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
problems.append(goObject)
go.GoGame.utility(goObject,'Def')

#Easy 22
dpiecestest = generateTuples('0312232406162636')
# white
apiecestest = generateTuples('011131223334454607172737')
dimstest = (5,8)
availstest = generateTuples('0204051314152535')
eyeSpotstest = generateTuples('03040513141525')
gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
problems.append(goObject)
go.GoGame.utility(goObject,'Def')

#Easy 27
dpiecestest = generateTuples('10115051524232')
# white
apiecestest = generateTuples('01121423334353606162')
dimstest = (8,5)
availstest = generateTuples('0020304021314122020313')
eyeSpotstest = generateTuples('203040213141')
gametest = [apiecestest, dpiecestest, availstest, eyeSpotstest, dimstest]
gamestatetest = goMain.generateInitialState(gametest[0], gametest[1], gametest[2], gametest[3], gametest[4])
goObject = go.GoGame(gamestatetest.player, gamestatetest.moves, gamestatetest.board, gamestatetest.connectedPieces, gamestatetest.survivalState, gamestatetest.eyes)
problems.append(goObject)
go.GoGame.utility(goObject,'Def')

#GpAndroid
#1289
