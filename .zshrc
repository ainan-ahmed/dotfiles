# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/ainan/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="powerlevel10k/powerlevel10k"
#ZSH_THEME="gruvbox"
# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" "powerlevel10k/powerlevel10k")

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
#DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"
# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-autosuggestions fast-syntax-highlighting virtualenv fzf)



# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
source $ZSH/oh-my-zsh.sh

source ~/.bash_profile
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
# neofetch
alias vim="nvim"
alias pacsize_top10="expac -H M '%m\t%n' | sort -hr | head -10"
alias swaymsgAllWindow="swaymsg -t get_tree | jq -r"
alias ls="eza --color=always --icons=always --long --no-permissions --no-user --no-time  --group-directories-first"
alias cd="z"
alias dcu="docker-compose up"
alias dcd="docker-compose down"
alias lzd="lazydocker"
alias lzg="lazygit"
alias kssh="kitten ssh"
alias CONNECT_DRACULA="kssh -i .ssh/OpenClaw-Home-World_key.pem  ainan@9.223.112.19"
zstyle ':completion:*' completer _expand_alias _complete _ignored
export EDITOR=/usr/bin/nvim
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

eval "$(zoxide init zsh)"

export QT_QPA_PLATFORM=wayland
eval "$(fzf --zsh)"
export PATH="$JAVA_HOME/bin:$PATH"
source /usr/share/nvm/init-nvm.sh
export FZF_DEFAULT_OPTS="
	--color=bg:#1d2021,bg+:#282828,spinner:#8ec07c,hl:#83a598
	--color=fg:#bdae93,header:#83a598,info:#fabd2f,pointer:#8ec07c
	--color=marker:#8ec07c,fg+:#d5c4a1,prompt:#fabd2f,hl+:#83a598"

function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}
export TERM=xterm
export CRYPTOGRAPHY_OPENSSL_NO_LEGACY=1
export GEMINI_API_KEY="AIzaSyCOlekQ6RDg9e2Z_A20j2JU4g8KCcv76B8"
export OPENCODE_ENABLE_EXA=1 opencode
#export OPENAI_API_KEY="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"

#export LANGSMITH_API_KEY="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"
#LANGSMITH_TRACING_V2=true
#LANGSMITH_PROJECT="langchain-academy"

#export TAVILY_API_KEY="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"
#export LANGFUSE_PUBLIC_KEY="pk-lf-4392d6f2-760e-4ae5-84ab-023ce482c705"
#export LANGFUSE_SECRET_KEY="sk-lf-dcf009f1-72ed-4747-9367-b6cf4ed50dc0"
#export LANGFUSE_HOST="https://cloud.langfuse.com"
#!/bin/sh
if [ "$TERM" = "linux" ]; then
	/bin/echo -e "
	\e]P0191724
	\e]P1eb6f92
	\e]P29ccfd8
	\e]P3f6c177
	\e]P431748f
	\e]P5c4a7e7
	\e]P6ebbcba
	\e]P7e0def4
	\e]P826233a
	\e]P9eb6f92
	\e]PA9ccfd8
	\e]PBf6c177
	\e]PC31748f
	\e]PDc4a7e7
	\e]PEebbcba
	\e]PFe0def4
	"
	# get rid of artifacts
	clear
fi
eval "$(uv generate-shell-completion zsh)"
eval "$(uvx --generate-shell-completion zsh)"

# Added by LM Studio CLI (lms)
export PATH="$PATH:/home/ainan/.lmstudio/bin"
# End of LM Studio CLI section


# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/ainan/google-cloud-sdk/path.zsh.inc' ]; then . '/home/ainan/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/ainan/google-cloud-sdk/completion.zsh.inc' ]; then . '/home/ainan/google-cloud-sdk/completion.zsh.inc'; fi
