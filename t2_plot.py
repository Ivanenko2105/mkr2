import matplotlib.pyplot as plt

def draw_t_1_fuzzy_area(x, mf):
    """
    Plots the Fuzzy Term.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r'$\mu$(x)')
    ax.set_xlabel('x')
    ax.set_ylim([0, 1.2])
    ax.plot(x, mf)
    ax.fill_between(x, mf)
    plt.grid(True)
    plt.show()


def draw_t2_fuzzy_set(x, lmf, umf):
    """
    Plots the T2 Fuzzy Set.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r'$\mu$(x)')
    ax.set_xlabel('x')
    ax.set_ylim([0, 1.2])

    ax.fill_between(x, lmf, umf, color="lightblue", edgecolor="b", alpha=.5)
    plt.grid(True)

    plt.show()


def draw_t2_fuzzy_term(x, lmf, umf, title: str):
    """
    Plots the T2 Fuzzy Term.
    """
    pass


def draw_words_model(words_model):
    """
    Plots the Linguistic Variable.
    """
    fig = plt.figure(figsize=(10, 5))
    plt.subplots_adjust(top=0.95, bottom=0.05, hspace=1.5, wspace=0.4)

    for number, word in enumerate(words_model['words'], start=1):
        ax = fig.add_subplot(8, 4, number)

        x = words_model['U']
        lmf, umf = words_model['words'][word]['lmf'], words_model['words'][word]['umf']

        ax.set_ylim([0, 1.2])
        ax.fill_between(x, lmf, umf, color="lightblue", edgecolor="b", alpha=.5)
        ax.set_title(word, fontsize=8)

    plt.grid(True)
    plt.show()


def draw_lv(lv):
    """
    Plots the Linguistic Variable.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r'$\mu$(x)')
    ax.set_xlabel('x')
    ax.set_ylim([0, 1.2])
    for term in lv['terms'].values():
        x = lv['U']
        lmf, umf = term['lmf'], term['umf']
        ax.set_ylim([0, 1.2])
        ax.fill_between(x, lmf, umf, color="lightblue", edgecolor="b", alpha=.5)

    plt.grid(True)
    plt.title(lv['name'])
    plt.show()

def draw_word(x, word: str, word_model):
    """
    Plots the Word.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r'$\mu$(x)')
    ax.set_xlabel('x')
    ax.set_ylim([0, 1.2])
    lmf, umf = word_model['lmf'], word_model['umf']
    ax.fill_between(x, lmf, umf, color="lightblue", edgecolor="b", alpha=.5)

    plt.grid(True)
    plt.show()