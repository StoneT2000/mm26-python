bfs_deltas = {
  128: [[0,0],[1,0],[0,-1],[-1,0],[0,1],[2,0],[1,-1],[0,-2],[-1,-1],[-2,0],[-1,1],[0,2],[1,1],[3,0],[2,-1],[1,-2],[0,-3],[-1,-2],[-2,-1],[-3,0],[-2,1],[-1,2],[0,3],[1,2],[2,1],[4,0],[3,-1],[2,-2],[1,-3],[0,-4],[-1,-3],[-2,-2],[-3,-1],[-4,0],[-3,1],[-2,2],[-1,3],[0,4],[1,3],[2,2],[3,1],[5,0],[4,-1],[3,-2],[2,-3],[1,-4],[0,-5],[-1,-4],[-2,-3],[-3,-2],[-4,-1],[-5,0],[-4,1],[-3,2],[-2,3],[-1,4],[0,5],[1,4],[2,3],[3,2],[4,1],[6,0],[5,-1],[4,-2],[3,-3],[2,-4],[1,-5],[0,-6],[-1,-5],[-2,-4],[-3,-3],[-4,-2],[-5,-1],[-6,0],[-5,1],[-4,2],[-3,3],[-2,4],[-1,5],[0,6],[1,5],[2,4],[3,3],[4,2],[5,1],[7,0],[6,-1],[5,-2],[4,-3],[3,-4],[2,-5],[1,-6],[0,-7],[-1,-6],[-2,-5],[-3,-4],[-4,-3],[-5,-2],[-6,-1],[-7,0],[-6,1],[-5,2],[-4,3],[-3,4],[-2,5],[-1,6],[0,7],[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[8,0],[7,-1],[6,-2],[5,-3],[4,-4],[3,-5],[2,-6],[1,-7],[0,-8],[-1,-7],[-2,-6],[-3,-5],[-4,-4],[-5,-3],[-6,-2],[-7,-1],[-8,0],[-7,1],[-6,2],[-5,3],[-4,4],[-3,5],[-2,6],[-1,7],[0,8],[1,7],[2,6],[3,5],[4,4],[5,3],[6,2],[7,1],[9,0],[8,-1],[7,-2],[6,-3],[5,-4],[4,-5],[3,-6],[2,-7],[1,-8],[0,-9],[-1,-8],[-2,-7],[-3,-6],[-4,-5],[-5,-4],[-6,-3],[-7,-2],[-8,-1],[-9,0],[-8,1],[-7,2],[-6,3],[-5,4],[-4,5],[-3,6],[-2,7],[-1,8],[0,9],[1,8],[2,7],[3,6],[4,5],[5,4],[6,3],[7,2],[8,1],[10,0],[9,-1],[8,-2],[7,-3],[6,-4],[5,-5],[4,-6],[3,-7],[2,-8],[1,-9],[0,-10],[-1,-9],[-2,-8],[-3,-7],[-4,-6],[-5,-5],[-6,-4],[-7,-3],[-8,-2],[-9,-1],[-10,0],[-9,1],[-8,2],[-7,3],[-6,4],[-5,5],[-4,6],[-3,7],[-2,8],[-1,9],[0,10],[1,9],[2,8],[3,7],[4,6],[5,5],[6,4],[7,3],[8,2],[9,1],[11,0],[10,-1],[9,-2],[8,-3],[7,-4],[6,-5],[5,-6],[4,-7],[3,-8],[2,-9],[1,-10],[0,-11],[-1,-10],[-2,-9],[-3,-8],[-4,-7],[-5,-6],[-6,-5],[-7,-4],[-8,-3],[-9,-2],[-10,-1],[-11,0],[-10,1],[-9,2],[-8,3],[-7,4],[-6,5],[-5,6],[-4,7],[-3,8],[-2,9],[-1,10],[0,11],[1,10],[2,9],[3,8],[4,7],[5,6],[6,5],[7,4],[8,3],[9,2],[10,1],[11,-1],[10,-2],[9,-3],[8,-4],[7,-5],[6,-6],[5,-7],[4,-8],[3,-9],[2,-10],[1,-11],[-1,-11],[-2,-10],[-3,-9],[-4,-8],[-5,-7],[-6,-6],[-7,-5],[-8,-4],[-9,-3],[-10,-2],[-11,-1],[-11,1],[-10,2],[-9,3],[-8,4],[-7,5],[-6,6],[-5,7],[-4,8],[-3,9],[-2,10],[-1,11],[1,11],[2,10],[3,9],[4,8],[5,7],[6,6],[7,5],[8,4],[9,3],[10,2],[11,1],[11,-2],[10,-3],[9,-4],[8,-5],[7,-6],[6,-7],[5,-8],[4,-9],[3,-10],[2,-11],[-2,-11],[-3,-10],[-4,-9],[-5,-8],[-6,-7],[-7,-6],[-8,-5],[-9,-4],[-10,-3],[-11,-2],[-11,2],[-10,3],[-9,4],[-8,5],[-7,6],[-6,7],[-5,8],[-4,9],[-3,10],[-2,11],[2,11],[3,10],[4,9],[5,8],[6,7],[7,6],[8,5],[9,4],[10,3],[11,2],[10,-4],[9,-5],[8,-6],[7,-7],[6,-8],[5,-9],[4,-10],[-4,-10],[-5,-9],[-6,-8],[-7,-7],[-8,-6],[-9,-5],[-10,-4],[-10,4],[-9,5],[-8,6],[-7,7],[-6,8],[-5,9],[-4,10],[4,10],[5,9],[6,8],[7,7],[8,6],[9,5],[10,4]],
  1024: [[0,0],[1,0],[0,-1],[-1,0],[0,1],[2,0],[1,-1],[0,-2],[-1,-1],[-2,0],[-1,1],[0,2],[1,1],[3,0],[2,-1],[1,-2],[0,-3],[-1,-2],[-2,-1],[-3,0],[-2,1],[-1,2],[0,3],[1,2],[2,1],[4,0],[3,-1],[2,-2],[1,-3],[0,-4],[-1,-3],[-2,-2],[-3,-1],[-4,0],[-3,1],[-2,2],[-1,3],[0,4],[1,3],[2,2],[3,1],[5,0],[4,-1],[3,-2],[2,-3],[1,-4],[0,-5],[-1,-4],[-2,-3],[-3,-2],[-4,-1],[-5,0],[-4,1],[-3,2],[-2,3],[-1,4],[0,5],[1,4],[2,3],[3,2],[4,1],[6,0],[5,-1],[4,-2],[3,-3],[2,-4],[1,-5],[0,-6],[-1,-5],[-2,-4],[-3,-3],[-4,-2],[-5,-1],[-6,0],[-5,1],[-4,2],[-3,3],[-2,4],[-1,5],[0,6],[1,5],[2,4],[3,3],[4,2],[5,1],[7,0],[6,-1],[5,-2],[4,-3],[3,-4],[2,-5],[1,-6],[0,-7],[-1,-6],[-2,-5],[-3,-4],[-4,-3],[-5,-2],[-6,-1],[-7,0],[-6,1],[-5,2],[-4,3],[-3,4],[-2,5],[-1,6],[0,7],[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[8,0],[7,-1],[6,-2],[5,-3],[4,-4],[3,-5],[2,-6],[1,-7],[0,-8],[-1,-7],[-2,-6],[-3,-5],[-4,-4],[-5,-3],[-6,-2],[-7,-1],[-8,0],[-7,1],[-6,2],[-5,3],[-4,4],[-3,5],[-2,6],[-1,7],[0,8],[1,7],[2,6],[3,5],[4,4],[5,3],[6,2],[7,1],[9,0],[8,-1],[7,-2],[6,-3],[5,-4],[4,-5],[3,-6],[2,-7],[1,-8],[0,-9],[-1,-8],[-2,-7],[-3,-6],[-4,-5],[-5,-4],[-6,-3],[-7,-2],[-8,-1],[-9,0],[-8,1],[-7,2],[-6,3],[-5,4],[-4,5],[-3,6],[-2,7],[-1,8],[0,9],[1,8],[2,7],[3,6],[4,5],[5,4],[6,3],[7,2],[8,1],[10,0],[9,-1],[8,-2],[7,-3],[6,-4],[5,-5],[4,-6],[3,-7],[2,-8],[1,-9],[0,-10],[-1,-9],[-2,-8],[-3,-7],[-4,-6],[-5,-5],[-6,-4],[-7,-3],[-8,-2],[-9,-1],[-10,0],[-9,1],[-8,2],[-7,3],[-6,4],[-5,5],[-4,6],[-3,7],[-2,8],[-1,9],[0,10],[1,9],[2,8],[3,7],[4,6],[5,5],[6,4],[7,3],[8,2],[9,1],[11,0],[10,-1],[9,-2],[8,-3],[7,-4],[6,-5],[5,-6],[4,-7],[3,-8],[2,-9],[1,-10],[0,-11],[-1,-10],[-2,-9],[-3,-8],[-4,-7],[-5,-6],[-6,-5],[-7,-4],[-8,-3],[-9,-2],[-10,-1],[-11,0],[-10,1],[-9,2],[-8,3],[-7,4],[-6,5],[-5,6],[-4,7],[-3,8],[-2,9],[-1,10],[0,11],[1,10],[2,9],[3,8],[4,7],[5,6],[6,5],[7,4],[8,3],[9,2],[10,1],[12,0],[11,-1],[10,-2],[9,-3],[8,-4],[7,-5],[6,-6],[5,-7],[4,-8],[3,-9],[2,-10],[1,-11],[0,-12],[-1,-11],[-2,-10],[-3,-9],[-4,-8],[-5,-7],[-6,-6],[-7,-5],[-8,-4],[-9,-3],[-10,-2],[-11,-1],[-12,0],[-11,1],[-10,2],[-9,3],[-8,4],[-7,5],[-6,6],[-5,7],[-4,8],[-3,9],[-2,10],[-1,11],[0,12],[1,11],[2,10],[3,9],[4,8],[5,7],[6,6],[7,5],[8,4],[9,3],[10,2],[11,1],[13,0],[12,-1],[11,-2],[10,-3],[9,-4],[8,-5],[7,-6],[6,-7],[5,-8],[4,-9],[3,-10],[2,-11],[1,-12],[0,-13],[-1,-12],[-2,-11],[-3,-10],[-4,-9],[-5,-8],[-6,-7],[-7,-6],[-8,-5],[-9,-4],[-10,-3],[-11,-2],[-12,-1],[-13,0],[-12,1],[-11,2],[-10,3],[-9,4],[-8,5],[-7,6],[-6,7],[-5,8],[-4,9],[-3,10],[-2,11],[-1,12],[0,13],[1,12],[2,11],[3,10],[4,9],[5,8],[6,7],[7,6],[8,5],[9,4],[10,3],[11,2],[12,1],[14,0],[13,-1],[12,-2],[11,-3],[10,-4],[9,-5],[8,-6],[7,-7],[6,-8],[5,-9],[4,-10],[3,-11],[2,-12],[1,-13],[0,-14],[-1,-13],[-2,-12],[-3,-11],[-4,-10],[-5,-9],[-6,-8],[-7,-7],[-8,-6],[-9,-5],[-10,-4],[-11,-3],[-12,-2],[-13,-1],[-14,0],[-13,1],[-12,2],[-11,3],[-10,4],[-9,5],[-8,6],[-7,7],[-6,8],[-5,9],[-4,10],[-3,11],[-2,12],[-1,13],[0,14],[1,13],[2,12],[3,11],[4,10],[5,9],[6,8],[7,7],[8,6],[9,5],[10,4],[11,3],[12,2],[13,1],[15,0],[14,-1],[13,-2],[12,-3],[11,-4],[10,-5],[9,-6],[8,-7],[7,-8],[6,-9],[5,-10],[4,-11],[3,-12],[2,-13],[1,-14],[0,-15],[-1,-14],[-2,-13],[-3,-12],[-4,-11],[-5,-10],[-6,-9],[-7,-8],[-8,-7],[-9,-6],[-10,-5],[-11,-4],[-12,-3],[-13,-2],[-14,-1],[-15,0],[-14,1],[-13,2],[-12,3],[-11,4],[-10,5],[-9,6],[-8,7],[-7,8],[-6,9],[-5,10],[-4,11],[-3,12],[-2,13],[-1,14],[0,15],[1,14],[2,13],[3,12],[4,11],[5,10],[6,9],[7,8],[8,7],[9,6],[10,5],[11,4],[12,3],[13,2],[14,1],[16,0],[15,-1],[14,-2],[13,-3],[12,-4],[11,-5],[10,-6],[9,-7],[8,-8],[7,-9],[6,-10],[5,-11],[4,-12],[3,-13],[2,-14],[1,-15],[0,-16],[-1,-15],[-2,-14],[-3,-13],[-4,-12],[-5,-11],[-6,-10],[-7,-9],[-8,-8],[-9,-7],[-10,-6],[-11,-5],[-12,-4],[-13,-3],[-14,-2],[-15,-1],[-16,0],[-15,1],[-14,2],[-13,3],[-12,4],[-11,5],[-10,6],[-9,7],[-8,8],[-7,9],[-6,10],[-5,11],[-4,12],[-3,13],[-2,14],[-1,15],[0,16],[1,15],[2,14],[3,13],[4,12],[5,11],[6,10],[7,9],[8,8],[9,7],[10,6],[11,5],[12,4],[13,3],[14,2],[15,1],[17,0],[16,-1],[15,-2],[14,-3],[13,-4],[12,-5],[11,-6],[10,-7],[9,-8],[8,-9],[7,-10],[6,-11],[5,-12],[4,-13],[3,-14],[2,-15],[1,-16],[0,-17],[-1,-16],[-2,-15],[-3,-14],[-4,-13],[-5,-12],[-6,-11],[-7,-10],[-8,-9],[-9,-8],[-10,-7],[-11,-6],[-12,-5],[-13,-4],[-14,-3],[-15,-2],[-16,-1],[-17,0],[-16,1],[-15,2],[-14,3],[-13,4],[-12,5],[-11,6],[-10,7],[-9,8],[-8,9],[-7,10],[-6,11],[-5,12],[-4,13],[-3,14],[-2,15],[-1,16],[0,17],[1,16],[2,15],[3,14],[4,13],[5,12],[6,11],[7,10],[8,9],[9,8],[10,7],[11,6],[12,5],[13,4],[14,3],[15,2],[16,1],[18,0],[17,-1],[16,-2],[15,-3],[14,-4],[13,-5],[12,-6],[11,-7],[10,-8],[9,-9],[8,-10],[7,-11],[6,-12],[5,-13],[4,-14],[3,-15],[2,-16],[1,-17],[0,-18],[-1,-17],[-2,-16],[-3,-15],[-4,-14],[-5,-13],[-6,-12],[-7,-11],[-8,-10],[-9,-9],[-10,-8],[-11,-7],[-12,-6],[-13,-5],[-14,-4],[-15,-3],[-16,-2],[-17,-1],[-18,0],[-17,1],[-16,2],[-15,3],[-14,4],[-13,5],[-12,6],[-11,7],[-10,8],[-9,9],[-8,10],[-7,11],[-6,12],[-5,13],[-4,14],[-3,15],[-2,16],[-1,17],[0,18],[1,17],[2,16],[3,15],[4,14],[5,13],[6,12],[7,11],[8,10],[9,9],[10,8],[11,7],[12,6],[13,5],[14,4],[15,3],[16,2],[17,1],[19,0],[18,-1],[17,-2],[16,-3],[15,-4],[14,-5],[13,-6],[12,-7],[11,-8],[10,-9],[9,-10],[8,-11],[7,-12],[6,-13],[5,-14],[4,-15],[3,-16],[2,-17],[1,-18],[0,-19],[-1,-18],[-2,-17],[-3,-16],[-4,-15],[-5,-14],[-6,-13],[-7,-12],[-8,-11],[-9,-10],[-10,-9],[-11,-8],[-12,-7],[-13,-6],[-14,-5],[-15,-4],[-16,-3],[-17,-2],[-18,-1],[-19,0],[-18,1],[-17,2],[-16,3],[-15,4],[-14,5],[-13,6],[-12,7],[-11,8],[-10,9],[-9,10],[-8,11],[-7,12],[-6,13],[-5,14],[-4,15],[-3,16],[-2,17],[-1,18],[0,19],[1,18],[2,17],[3,16],[4,15],[5,14],[6,13],[7,12],[8,11],[9,10],[10,9],[11,8],[12,7],[13,6],[14,5],[15,4],[16,3],[17,2],[18,1],[20,0],[19,-1],[18,-2],[17,-3],[16,-4],[15,-5],[14,-6],[13,-7],[12,-8],[11,-9],[10,-10],[9,-11],[8,-12],[7,-13],[6,-14],[5,-15],[4,-16],[3,-17],[2,-18],[1,-19],[0,-20],[-1,-19],[-2,-18],[-3,-17],[-4,-16],[-5,-15],[-6,-14],[-7,-13],[-8,-12],[-9,-11],[-10,-10],[-11,-9],[-12,-8],[-13,-7],[-14,-6],[-15,-5],[-16,-4],[-17,-3],[-18,-2],[-19,-1],[-20,0],[-19,1],[-18,2],[-17,3],[-16,4],[-15,5],[-14,6],[-13,7],[-12,8],[-11,9],[-10,10],[-9,11],[-8,12],[-7,13],[-6,14],[-5,15],[-4,16],[-3,17],[-2,18],[-1,19],[0,20],[1,19],[2,18],[3,17],[4,16],[5,15],[6,14],[7,13],[8,12],[9,11],[10,10],[11,9],[12,8],[13,7],[14,6],[15,5],[16,4],[17,3],[18,2],[19,1],[21,0],[20,-1],[19,-2],[18,-3],[17,-4],[16,-5],[15,-6],[14,-7],[13,-8],[12,-9],[11,-10],[10,-11],[9,-12],[8,-13],[7,-14],[6,-15],[5,-16],[4,-17],[3,-18],[2,-19],[1,-20],[0,-21],[-1,-20],[-2,-19],[-3,-18],[-4,-17],[-5,-16],[-6,-15],[-7,-14],[-8,-13],[-9,-12],[-10,-11],[-11,-10],[-12,-9],[-13,-8],[-14,-7],[-15,-6],[-16,-5],[-17,-4],[-18,-3],[-19,-2],[-20,-1],[-21,0],[-20,1],[-19,2],[-18,3],[-17,4],[-16,5],[-15,6],[-14,7],[-13,8],[-12,9],[-11,10],[-10,11],[-9,12],[-8,13],[-7,14],[-6,15],[-5,16],[-4,17],[-3,18],[-2,19],[-1,20],[0,21],[1,20],[2,19],[3,18],[4,17],[5,16],[6,15],[7,14],[8,13],[9,12],[10,11],[11,10],[12,9],[13,8],[14,7],[15,6],[16,5],[17,4],[18,3],[19,2],[20,1],[22,0],[21,-1],[20,-2],[19,-3],[18,-4],[17,-5],[16,-6],[15,-7],[14,-8],[13,-9],[12,-10],[11,-11],[10,-12],[9,-13],[8,-14],[7,-15],[6,-16],[5,-17],[4,-18],[3,-19],[2,-20],[1,-21],[0,-22],[-1,-21],[-2,-20],[-3,-19],[-4,-18],[-5,-17],[-6,-16],[-7,-15],[-8,-14],[-9,-13],[-10,-12],[-11,-11],[-12,-10],[-13,-9],[-14,-8],[-15,-7],[-16,-6],[-17,-5],[-18,-4],[-19,-3],[-20,-2],[-21,-1],[-22,0],[-21,1],[-20,2],[-19,3],[-18,4],[-17,5],[-16,6],[-15,7],[-14,8],[-13,9],[-12,10],[-11,11],[-10,12],[-9,13],[-8,14],[-7,15],[-6,16],[-5,17],[-4,18],[-3,19],[-2,20],[-1,21],[0,22],[1,21],[2,20],[3,19],[4,18],[5,17],[6,16],[7,15],[8,14],[9,13],[10,12],[11,11],[12,10],[13,9],[14,8],[15,7],[16,6],[17,5],[18,4],[19,3],[20,2],[21,1],[23,0],[22,-1],[21,-2],[20,-3],[19,-4],[18,-5],[17,-6],[16,-7],[15,-8],[14,-9],[13,-10],[12,-11],[11,-12],[10,-13],[9,-14],[8,-15],[7,-16],[6,-17],[5,-18],[4,-19],[3,-20],[2,-21],[1,-22],[0,-23],[-1,-22],[-2,-21],[-3,-20],[-4,-19],[-5,-18],[-6,-17],[-7,-16],[-8,-15],[-9,-14],[-10,-13],[-11,-12],[-12,-11],[-13,-10],[-14,-9],[-15,-8],[-16,-7],[-17,-6],[-18,-5],[-19,-4],[-20,-3],[-21,-2],[-22,-1],[-23,0],[-22,1],[-21,2],[-20,3],[-19,4],[-18,5],[-17,6],[-16,7],[-15,8],[-14,9],[-13,10],[-12,11],[-11,12],[-10,13],[-9,14],[-8,15],[-7,16],[-6,17],[-5,18],[-4,19],[-3,20],[-2,21],[-1,22],[0,23],[1,22],[2,21],[3,20],[4,19],[5,18],[6,17],[7,16],[8,15],[9,14],[10,13],[11,12],[12,11],[13,10],[14,9],[15,8],[16,7],[17,6],[18,5],[19,4],[20,3],[21,2],[22,1],[24,0],[23,-1],[22,-2],[21,-3],[20,-4],[19,-5],[18,-6],[17,-7],[16,-8],[15,-9],[14,-10],[13,-11],[12,-12],[11,-13],[10,-14],[9,-15],[8,-16],[7,-17],[6,-18],[5,-19],[4,-20],[3,-21],[2,-22],[1,-23],[0,-24],[-1,-23],[-2,-22],[-3,-21],[-4,-20],[-5,-19],[-6,-18],[-7,-17],[-8,-16],[-9,-15],[-10,-14],[-11,-13],[-12,-12],[-13,-11],[-14,-10],[-15,-9],[-16,-8],[-17,-7],[-18,-6],[-19,-5],[-20,-4],[-21,-3],[-22,-2],[-23,-1],[-24,0],[-23,1],[-22,2],[-21,3],[-20,4],[-19,5],[-18,6],[-17,7],[-16,8],[-15,9],[-14,10],[-13,11],[-12,12],[-11,13],[-10,14],[-9,15],[-8,16],[-7,17],[-6,18],[-5,19],[-4,20],[-3,21],[-2,22],[-1,23],[0,24],[1,23],[2,22],[3,21],[4,20],[5,19],[6,18],[7,17],[8,16],[9,15],[10,14],[11,13],[12,12],[13,11],[14,10],[15,9],[16,8],[17,7],[18,6],[19,5],[20,4],[21,3],[22,2],[23,1],[25,0],[24,-1],[23,-2],[22,-3],[21,-4],[20,-5],[19,-6],[18,-7],[17,-8],[16,-9],[15,-10],[14,-11],[13,-12],[12,-13],[11,-14],[10,-15],[9,-16],[8,-17],[7,-18],[6,-19],[5,-20],[4,-21],[3,-22],[2,-23],[1,-24],[0,-25],[-1,-24],[-2,-23],[-3,-22],[-4,-21],[-5,-20],[-6,-19],[-7,-18],[-8,-17],[-9,-16],[-10,-15],[-11,-14],[-12,-13],[-13,-12],[-14,-11],[-15,-10],[-16,-9],[-17,-8],[-18,-7],[-19,-6],[-20,-5],[-21,-4],[-22,-3],[-23,-2],[-24,-1],[-25,0],[-24,1],[-23,2],[-22,3],[-21,4],[-20,5],[-19,6],[-18,7],[-17,8],[-16,9],[-15,10],[-14,11],[-13,12],[-12,13],[-11,14],[-10,15],[-9,16],[-8,17],[-7,18],[-6,19],[-5,20],[-4,21],[-3,22],[-2,23],[-1,24],[0,25],[1,24],[2,23],[3,22],[4,21],[5,20],[6,19],[7,18],[8,17],[9,16],[10,15],[11,14],[12,13],[13,12],[14,11],[15,10],[16,9],[17,8],[18,7],[19,6],[20,5],[21,4],[22,3],[23,2],[24,1],[26,0],[25,-1],[24,-2],[23,-3],[22,-4],[21,-5],[20,-6],[19,-7],[18,-8],[17,-9],[16,-10],[15,-11],[14,-12],[13,-13],[12,-14],[11,-15],[10,-16],[9,-17],[8,-18],[7,-19],[6,-20],[5,-21],[4,-22],[3,-23],[2,-24],[1,-25],[0,-26],[-1,-25],[-2,-24],[-3,-23],[-4,-22],[-5,-21],[-6,-20],[-7,-19],[-8,-18],[-9,-17],[-10,-16],[-11,-15],[-12,-14],[-13,-13],[-14,-12],[-15,-11],[-16,-10],[-17,-9],[-18,-8],[-19,-7],[-20,-6],[-21,-5],[-22,-4],[-23,-3],[-24,-2],[-25,-1],[-26,0],[-25,1],[-24,2],[-23,3],[-22,4],[-21,5],[-20,6],[-19,7],[-18,8],[-17,9],[-16,10],[-15,11],[-14,12],[-13,13],[-12,14],[-11,15],[-10,16],[-9,17],[-8,18],[-7,19],[-6,20],[-5,21],[-4,22],[-3,23],[-2,24],[-1,25],[0,26],[1,25],[2,24],[3,23],[4,22],[5,21],[6,20],[7,19],[8,18],[9,17],[10,16],[11,15],[12,14],[13,13],[14,12],[15,11],[16,10],[17,9],[18,8],[19,7],[20,6],[21,5],[22,4],[23,3],[24,2],[25,1],[27,0],[26,-1],[25,-2],[24,-3],[23,-4],[22,-5],[21,-6],[20,-7],[19,-8],[18,-9],[17,-10],[16,-11],[15,-12],[14,-13],[13,-14],[12,-15],[11,-16],[10,-17],[9,-18],[8,-19],[7,-20],[6,-21],[5,-22],[4,-23],[3,-24],[2,-25],[1,-26],[0,-27],[-1,-26],[-2,-25],[-3,-24],[-4,-23],[-5,-22],[-6,-21],[-7,-20],[-8,-19],[-9,-18],[-10,-17],[-11,-16],[-12,-15],[-13,-14],[-14,-13],[-15,-12],[-16,-11],[-17,-10],[-18,-9],[-19,-8],[-20,-7],[-21,-6],[-22,-5],[-23,-4],[-24,-3],[-25,-2],[-26,-1],[-27,0],[-26,1],[-25,2],[-24,3],[-23,4],[-22,5],[-21,6],[-20,7],[-19,8],[-18,9],[-17,10],[-16,11],[-15,12],[-14,13],[-13,14],[-12,15],[-11,16],[-10,17],[-9,18],[-8,19],[-7,20],[-6,21],[-5,22],[-4,23],[-3,24],[-2,25],[-1,26],[0,27],[1,26],[2,25],[3,24],[4,23],[5,22],[6,21],[7,20],[8,19],[9,18],[10,17],[11,16],[12,15],[13,14],[14,13],[15,12],[16,11],[17,10],[18,9],[19,8],[20,7],[21,6],[22,5],[23,4],[24,3],[25,2],[26,1],[28,0],[27,-1],[26,-2],[25,-3],[24,-4],[23,-5],[22,-6],[21,-7],[20,-8],[19,-9],[18,-10],[17,-11],[16,-12],[15,-13],[14,-14],[13,-15],[12,-16],[11,-17],[10,-18],[9,-19],[8,-20],[7,-21],[6,-22],[5,-23],[4,-24],[3,-25],[2,-26],[1,-27],[0,-28],[-1,-27],[-2,-26],[-3,-25],[-4,-24],[-5,-23],[-6,-22],[-7,-21],[-8,-20],[-9,-19],[-10,-18],[-11,-17],[-12,-16],[-13,-15],[-14,-14],[-15,-13],[-16,-12],[-17,-11],[-18,-10],[-19,-9],[-20,-8],[-21,-7],[-22,-6],[-23,-5],[-24,-4],[-25,-3],[-26,-2],[-27,-1],[-28,0],[-27,1],[-26,2],[-25,3],[-24,4],[-23,5],[-22,6],[-21,7],[-20,8],[-19,9],[-18,10],[-17,11],[-16,12],[-15,13],[-14,14],[-13,15],[-12,16],[-11,17],[-10,18],[-9,19],[-8,20],[-7,21],[-6,22],[-5,23],[-4,24],[-3,25],[-2,26],[-1,27],[0,28],[1,27],[2,26],[3,25],[4,24],[5,23],[6,22],[7,21],[8,20],[9,19],[10,18],[11,17],[12,16],[13,15],[14,14],[15,13],[16,12],[17,11],[18,10],[19,9],[20,8],[21,7],[22,6],[23,5],[24,4],[25,3],[26,2],[27,1],[29,0],[28,-1],[27,-2],[26,-3],[25,-4],[24,-5],[23,-6],[22,-7],[21,-8],[20,-9],[19,-10],[18,-11],[17,-12],[16,-13],[15,-14],[14,-15],[13,-16],[12,-17],[11,-18],[10,-19],[9,-20],[8,-21],[7,-22],[6,-23],[5,-24],[4,-25],[3,-26],[2,-27],[1,-28],[0,-29],[-1,-28],[-2,-27],[-3,-26],[-4,-25],[-5,-24],[-6,-23],[-7,-22],[-8,-21],[-9,-20],[-10,-19],[-11,-18],[-12,-17],[-13,-16],[-14,-15],[-15,-14],[-16,-13],[-17,-12],[-18,-11],[-19,-10],[-20,-9],[-21,-8],[-22,-7],[-23,-6],[-24,-5],[-25,-4],[-26,-3],[-27,-2],[-28,-1],[-29,0],[-28,1],[-27,2],[-26,3],[-25,4],[-24,5],[-23,6],[-22,7],[-21,8],[-20,9],[-19,10],[-18,11],[-17,12],[-16,13],[-15,14],[-14,15],[-13,16],[-12,17],[-11,18],[-10,19],[-9,20],[-8,21],[-7,22],[-6,23],[-5,24],[-4,25],[-3,26],[-2,27],[-1,28],[0,29],[1,28],[2,27],[3,26],[4,25],[5,24],[6,23],[7,22],[8,21],[9,20],[10,19],[11,18],[12,17],[13,16],[14,15],[15,14],[16,13],[17,12],[18,11],[19,10],[20,9],[21,8],[22,7],[23,6],[24,5],[25,4],[26,3],[27,2],[28,1],[30,0],[29,-1],[28,-2],[27,-3],[26,-4],[25,-5],[24,-6],[23,-7],[22,-8],[21,-9],[20,-10],[19,-11],[18,-12],[17,-13],[16,-14],[15,-15],[14,-16],[13,-17],[12,-18],[11,-19],[10,-20],[9,-21],[8,-22],[7,-23],[6,-24],[5,-25],[4,-26],[3,-27],[2,-28],[1,-29],[0,-30],[-1,-29],[-2,-28],[-3,-27],[-4,-26],[-5,-25],[-6,-24],[-7,-23],[-8,-22],[-9,-21],[-10,-20],[-11,-19],[-12,-18],[-13,-17],[-14,-16],[-15,-15],[-16,-14],[-17,-13],[-18,-12],[-19,-11],[-20,-10],[-21,-9],[-22,-8],[-23,-7],[-24,-6],[-25,-5],[-26,-4],[-27,-3],[-28,-2],[-29,-1],[-30,0],[-29,1],[-28,2],[-27,3],[-26,4],[-25,5],[-24,6],[-23,7],[-22,8],[-21,9],[-20,10],[-19,11],[-18,12],[-17,13],[-16,14],[-15,15],[-14,16],[-13,17],[-12,18],[-11,19],[-10,20],[-9,21],[-8,22],[-7,23],[-6,24],[-5,25],[-4,26],[-3,27],[-2,28],[-1,29],[0,30],[1,29],[2,28],[3,27],[4,26],[5,25],[6,24],[7,23],[8,22],[9,21],[10,20],[11,19],[12,18],[13,17],[14,16],[15,15],[16,14],[17,13],[18,12],[19,11],[20,10],[21,9],[22,8],[23,7],[24,6],[25,5],[26,4],[27,3],[28,2],[29,1],[31,0],[30,-1],[29,-2],[28,-3],[27,-4],[26,-5],[25,-6],[24,-7],[23,-8],[22,-9],[21,-10],[20,-11],[19,-12],[18,-13],[17,-14],[16,-15],[15,-16],[14,-17],[13,-18],[12,-19],[11,-20],[10,-21],[9,-22],[8,-23],[7,-24],[6,-25],[5,-26],[4,-27],[3,-28],[2,-29],[1,-30],[0,-31],[-1,-30],[-2,-29],[-3,-28],[-4,-27],[-5,-26],[-6,-25],[-7,-24],[-8,-23],[-9,-22],[-10,-21],[-11,-20],[-12,-19],[-13,-18],[-14,-17],[-15,-16],[-16,-15],[-17,-14],[-18,-13],[-19,-12],[-20,-11],[-21,-10],[-22,-9],[-23,-8],[-24,-7],[-25,-6],[-26,-5],[-27,-4],[-28,-3],[-29,-2],[-30,-1],[-31,0],[-30,1],[-29,2],[-28,3],[-27,4],[-26,5],[-25,6],[-24,7],[-23,8],[-22,9],[-21,10],[-20,11],[-19,12],[-18,13],[-17,14],[-16,15],[-15,16],[-14,17],[-13,18],[-12,19],[-11,20],[-10,21],[-9,22],[-8,23],[-7,24],[-6,25],[-5,26],[-4,27],[-3,28],[-2,29],[-1,30],[0,31],[1,30],[2,29],[3,28],[4,27],[5,26],[6,25],[7,24],[8,23],[9,22],[10,21],[11,20],[12,19],[13,18],[14,17],[15,16],[16,15],[17,14],[18,13],[19,12],[20,11],[21,10],[22,9],[23,8],[24,7],[25,6],[26,5],[27,4],[28,3],[29,2],[30,1],[32,0],[31,-1],[30,-2],[29,-3],[28,-4],[27,-5],[26,-6],[25,-7],[24,-8],[23,-9],[22,-10],[21,-11],[20,-12],[19,-13],[18,-14],[17,-15],[16,-16],[15,-17],[14,-18],[13,-19],[12,-20],[11,-21],[10,-22],[9,-23],[8,-24],[7,-25],[6,-26],[5,-27],[4,-28],[3,-29],[2,-30],[1,-31],[0,-32],[-1,-31],[-2,-30],[-3,-29],[-4,-28],[-5,-27],[-6,-26],[-7,-25],[-8,-24],[-9,-23],[-10,-22],[-11,-21],[-12,-20],[-13,-19],[-14,-18],[-15,-17],[-16,-16],[-17,-15],[-18,-14],[-19,-13],[-20,-12],[-21,-11],[-22,-10],[-23,-9],[-24,-8],[-25,-7],[-26,-6],[-27,-5],[-28,-4],[-29,-3],[-30,-2],[-31,-1],[-32,0],[-31,1],[-30,2],[-29,3],[-28,4],[-27,5],[-26,6],[-25,7],[-24,8],[-23,9],[-22,10],[-21,11],[-20,12],[-19,13],[-18,14],[-17,15],[-16,16],[-15,17],[-14,18],[-13,19],[-12,20],[-11,21],[-10,22],[-9,23],[-8,24],[-7,25],[-6,26],[-5,27],[-4,28],[-3,29],[-2,30],[-1,31],[0,32],[1,31],[2,30],[3,29],[4,28],[5,27],[6,26],[7,25],[8,24],[9,23],[10,22],[11,21],[12,20],[13,19],[14,18],[15,17],[16,16],[17,15],[18,14],[19,13],[20,12],[21,11],[22,10],[23,9],[24,8],[25,7],[26,6],[27,5],[28,4],[29,3],[30,2],[31,1],[31,-2],[30,-3],[29,-4],[28,-5],[27,-6],[26,-7],[25,-8],[24,-9],[23,-10],[22,-11],[21,-12],[20,-13],[19,-14],[18,-15],[17,-16],[16,-17],[15,-18],[14,-19],[13,-20],[12,-21],[11,-22],[10,-23],[9,-24],[8,-25],[7,-26],[6,-27],[5,-28],[4,-29],[3,-30],[2,-31],[-2,-31],[-3,-30],[-4,-29],[-5,-28],[-6,-27],[-7,-26],[-8,-25],[-9,-24],[-10,-23],[-11,-22],[-12,-21],[-13,-20],[-14,-19],[-15,-18],[-16,-17],[-17,-16],[-18,-15],[-19,-14],[-20,-13],[-21,-12],[-22,-11],[-23,-10],[-24,-9],[-25,-8],[-26,-7],[-27,-6],[-28,-5],[-29,-4],[-30,-3],[-31,-2],[-31,2],[-30,3],[-29,4],[-28,5],[-27,6],[-26,7],[-25,8],[-24,9],[-23,10],[-22,11],[-21,12],[-20,13],[-19,14],[-18,15],[-17,16],[-16,17],[-15,18],[-14,19],[-13,20],[-12,21],[-11,22],[-10,23],[-9,24],[-8,25],[-7,26],[-6,27],[-5,28],[-4,29],[-3,30],[-2,31],[2,31],[3,30],[4,29],[5,28],[6,27],[7,26],[8,25],[9,24],[10,23],[11,22],[12,21],[13,20],[14,19],[15,18],[16,17],[17,16],[18,15],[19,14],[20,13],[21,12],[22,11],[23,10],[24,9],[25,8],[26,7],[27,6],[28,5],[29,4],[30,3],[31,2],[31,-3],[30,-4],[29,-5],[28,-6],[27,-7],[26,-8],[25,-9],[24,-10],[23,-11],[22,-12],[21,-13],[20,-14],[19,-15],[18,-16],[17,-17],[16,-18],[15,-19],[14,-20],[13,-21],[12,-22],[11,-23],[10,-24],[9,-25],[8,-26],[7,-27],[6,-28],[5,-29],[4,-30],[3,-31],[-3,-31],[-4,-30],[-5,-29],[-6,-28],[-7,-27],[-8,-26],[-9,-25],[-10,-24],[-11,-23],[-12,-22],[-13,-21],[-14,-20],[-15,-19],[-16,-18],[-17,-17],[-18,-16],[-19,-15],[-20,-14],[-21,-13],[-22,-12],[-23,-11],[-24,-10],[-25,-9],[-26,-8],[-27,-7],[-28,-6],[-29,-5],[-30,-4],[-31,-3],[-31,3],[-30,4],[-29,5],[-28,6],[-27,7],[-26,8],[-25,9],[-24,10],[-23,11],[-22,12],[-21,13],[-20,14],[-19,15],[-18,16],[-17,17],[-16,18],[-15,19],[-14,20],[-13,21],[-12,22],[-11,23],[-10,24],[-9,25],[-8,26],[-7,27],[-6,28],[-5,29],[-4,30],[-3,31],[3,31],[4,30],[5,29],[6,28],[7,27],[8,26],[9,25],[10,24],[11,23],[12,22],[13,21],[14,20],[15,19],[16,18],[17,17],[18,16],[19,15],[20,14],[21,13],[22,12],[23,11],[24,10],[25,9],[26,8],[27,7],[28,6],[29,5],[30,4],[31,3]]
}