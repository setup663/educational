class Sorter:
    def sorting(self, d, file):
        f_out = open(file, 'w', encoding='UTF-8')
        f_out.write('Читатель Количество\n')
        for k in sorted(d):
            f_out.write(k + ' ' + str(d[k]) + '\n')
        f_out.close()
        return